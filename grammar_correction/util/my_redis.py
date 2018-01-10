# -*- coding:utf-8 -*-

"""
主要是Redis的一些相关操作
"""

import redis
import simplejson


class Redis(object):

    def __init__(self):
        self.MAX_VALID_TIME = 3600
        pool = redis.ConnectionPool(host='localhost', port=6380, decode_responses=True)
        self.redis_conn = redis.Redis(connection_pool=pool)

    def is_exist_token(self, token):
        """
        查询token是否在redis中，如果在表示该用户已经登录且token还在有效期
        :param token: token值
        :return: 存在返回True，否则False
        """
        try:
            query_res = self.redis_conn.get(token)
            if query_res:
                return True
            else:
                return False
        except:
            return False

    def add_token_record(self, token, data):
        """
        添加token及相应的data到redis中
        :param token: type str "123cvrt56"
        :param data: json_dict {"user_name": "zhangsan", "user_type": 0}
        :return: 添加成功返回True，其他False
        """
        try:
            self.redis_conn.set(name=token, value=simplejson.dumps(data), ex=self.MAX_VALID_TIME)
            return True
        except Exception:
            return False

    def delete_token(self, token):
        """
        从redis中删除token，比如说用于用户退出登录
        :param token: token值
        :return: 删除成功返回0，不存在返回1，删除中发生异常返回-1
        """
        try:
            res_code = self.redis_conn.delete(token)
            if res_code == 1:
                return 0
            else:
                return 1
        except:
            print("Exception in delete token from redis!")
            return -1
