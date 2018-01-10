# -*- coding:utf-8 -*-

import redis
import simplejson
import json

pool = redis.ConnectionPool(host='localhost', port=6380, decode_responses=True)
redis_conn = redis.Redis(connection_pool=pool)

key = "1"
value = {
    "user_name": "zhangsan",
    "user_type": 0,
}
redis_conn.set(name=key, value=json.dumps(value))

res = redis_conn.get(key)

print(type(res))
print(res)

tmp = '{"user_name": "zhangsan", "user_type": 0}'
res_dict = json.loads(res)
# print(res_dict['user_name'])
print(res_dict)

res = redis_conn.delete("4")
print(res)
print(redis_conn.get("2"))