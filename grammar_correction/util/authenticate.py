# -*- coding:utf-8 -*-
from itsdangerous import SignatureExpired, BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from grammar_correction.util import config


def gen_token(user_name, password):
    dump_str = user_name + password
    s = Serializer(secret_key=config.SECRET_KEY, salt=config.AUTH_SALT)
    return s.dumps(dump_str)


def verify_auth_token(token):
    s = Serializer(secret_key=config.SECRET_KEY, salt=config.AUTH_SALT)
    try:
        data = s.loads(token)
        print('data:', data)
    except SignatureExpired:
        return 0  # valid token, but expired
    except BadSignature:
        return -1  # invalid token
    return 2


# def generate_new_token(user_name, passwd):
#     user = User.objects.get(user_name=user_name, password=passwd)
#     default_token_generator.make_token(user)
#     cache.__setattr__()

if __name__=='__main__':
    token = gen_token("name", "123")
    print(token)
    code = verify_auth_token(token)
    print(code)