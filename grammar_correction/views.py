from django.shortcuts import render
from django.shortcuts import HttpResponse

from grammar_correction.models import User, FeedbackResult
from grammar_correction.util import authenticate

# Create your views here.
import json
import simplejson

from gingerit.gingerit import GingerIt
from grammar_correction.util.my_redis import Redis

redis = Redis()


def handle_login(user_name, password, user_type):
    """
    处理登录，在验证了用户名和密码之后生成token，以及将token存入redis
    :param user_name: 用户名
    :param password: 密码
    :return: token
    """
    # print('user_name: ', user_name)
    # print('password: ', password)
    # print('user_type: ', user_type)
    token = authenticate.gen_token(user_name=user_name, password=password)
    data = {
        "user_name": user_name,
        "user_type": user_type
    }
    global redis
    is_exist_token = redis.is_exist_token(token=token)
    if not is_exist_token: # redis 中还不存在该token，也就是用户没有登录
        if redis.add_token_record(token=token, data=data):
            print("Success to add token data to redis!")
            return token
        else:
            print("Fail to add token data to redis!")
            return None
    else:
        print("Token is already in redis.")
        return token


def login(request):
    if request.method == 'POST':
        result = {}
        try:
            data = simplejson.loads(request.body)
            user_name = data['user_name']
            password = data['password']
            user = User.objects.filter(user_name=user_name, password=password)
            if user:  # 用户名和密码正确
                token = handle_login(user_name=user_name, password=password, user_type=user[0].user_type)
                if token:
                    result['code'] = 0  # 正确登录
                    result['token'] = token
                    result['data'] = {}
                    result['data']['user_type'] = user[0].user_type

                    # print(111111)
                    # response = HttpResponse(json.dumps(result, ensure_ascii=False))
                    #
                    # return response
                else:
                    result['code'] = -1  # 服务器内部错误
            else:
                if User.objects.filter(user_name=user_name):  # 用户名和密码错误
                    result['code'] = 1
                else:  # 用户不存在
                    result['code'] = 2
        except Exception as e:
            print("Exception in parse login data!")
            print("Exception: ", e)
        finally:
            # print("result: ", result)
            response = HttpResponse(json.dumps(result, ensure_ascii=False))

            return response
    else:
        print("GET")
        response = HttpResponse(json.dumps({"code": -1}, ensure_ascii=False))
        return response


def verify_logged_in(request):
    """
    验证用户是否已经登录
    :param request: 网络请求
    :return: 已经登录返回True,其他返回False
    """
    token = request.META.get("HTTP_ACCESS_TOKEN")
    # print("get token token: ", token)
    # print("token type: ", type(token))

    global redis
    is_exist_token = redis.is_exist_token(token=token)
    if is_exist_token:
        print("already login")
    else:
        print("not login")
    return is_exist_token


def correct_grammatical_mistake(request):
    # if not verify_logged_in(request):  # 未登录
    #     result = {}
    #     result['code'] = 1
    #     response = HttpResponse(json.dumps(result, ensure_ascii=False))
    #
    #     return response
    data = simplejson.loads(request.body)
    text = data['gcSource']

    # parser = GingerIt()
    # gc_res = parser.parse(text)

    result = {}
    result['code'] = 0
    result['data'] = {}
    # result['data']['gcResult'] = gc_res["result"]
    result['data']['gcResult'] = text

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    # response['Access-Control-Allow-Origin'] = '*'

    return response

def gc_correct_suggest(request):
    if not verify_logged_in(request):  # 未登录
        return HttpResponse(json.dumps({"code": 1}, ensure_ascii=False))

    data = simplejson.loads(request.body)
    print("suggest data = {}".format(data))

    token = request.META.get("HTTP_ACCESS_TOKEN")
    print("token = {}".format(token))
    user_data = redis.get_data(token=token)
    print("user_data = {}".format(user_data))
    print(type(user_data))
    user_name = user_data["user_name"]
    print("user_name = {}".format(user_name))

    db = FeedbackResult(user_name=user_name, original_text=data["gcSource"],
                        system_correction_result=data["gcRes"],
                        user_correction_suggestion=data["gcResSugg"])
    db.save()

    result = {'code': 0}

    return HttpResponse(json.dumps(result, ensure_ascii=False))