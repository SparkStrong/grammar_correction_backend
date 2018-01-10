from django.shortcuts import render
from django.shortcuts import HttpResponse

from grammar_correction.models import User
from grammar_correction.util import authenticate

# Create your views here.
import json
import simplejson

from gingerit.gingerit import GingerIt


def handle_login(user_name, password, user_type):
    """
    处理登录，在验证了用户名和密码之后生成token，以及将token存入redis
    :param user_name: 用户名
    :param password: 密码
    :return: token
    """
    token = authenticate.gen_token(user_name=user_name, password=password)
    data = {
        "user_name": user_name,
        "user_type": user_type
    }



def login(request):
    if request.POST:
        result = {}

        try:
            data = simplejson.loads(request.body)
            user_name = data['user_name']
            password = data['password']
            user = User.objects.filter(user_name=user_name, password=password)
            if user:
                # 登录成功
                result['code'] = 0
                result['data']['user_type'] = user[0].user_type

        except Exception as e:
            print("Exception in parse login data!")
            print("Exception: ", e)

def get_token(request):
    token = request.META.get("Access-Token")
    print(token)

    return token


def correct_grammatical_mistake(request):
    # token = get_token(request)
    # data = json.load(request.body)
    data = simplejson.loads(request.body)
    text = data['gcSource']

    parser = GingerIt()
    gc_res = parser.parse(text)

    result = {}
    result['code'] = 0
    result['data'] = {}
    result['data']['gcResult'] = gc_res["result"]

    response = HttpResponse(json.dumps(result, ensure_ascii=False))
    # response['Access-Control-Allow-Origin'] = '*'

    return response
