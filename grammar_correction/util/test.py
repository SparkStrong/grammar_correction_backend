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




from nltk.tokenize import sent_tokenize

def sentence_token_nltk(str):
    sent_tokenize_list = sent_tokenize(str)
    return sent_tokenize_list

sentence = "This is a sentence by Mr. Smith from the U.S.A. This is another sentence. A third one; Using a semicolon?"

result = sentence_token_nltk(sentence)

print(result)


# path_to_jar = 'D:\software\StandfordNLP\stanford-parser-full-2017-06-09\stanford-parser.jar'
# path_to_model_jar = 'D:\software\StandfordNLP\stanford-parser-full-2017-06-09\stanford-parser-3.8.0-models.jar'
# model_path = 'D:\software\StandfordNLP\stanford-parser-full-2017-06-09\stanford-parser-3.8.0-models.jar\edu\stanford' \
#              '\nlp\models\lexparser\englishPCFG.ser.gz'

# s = "the quick brown fox jumps over the lazy dog"
#
# # 依存分析
# from nltk.parse.stanford import StanfordDependencyParser
# parser = StanfordDependencyParser(path_to_jar, path_to_model_jar, model_path)
# result = list(parser.parse(s.split()))
# for row in result[0].triples():
#     print(row)
#
# # 句法结构分析
# from nltk.parse.stanford import StanfordParser
# parser = StanfordParser(path_to_jar, path_to_model_jar, model_path)
# result = list(parser.parse(s.split()))
# for r in result:
#     print(r)
#     print(r.draw())

# from nltk.parse.stanford import StanfordParser
# eng_parser = StanfordParser(r"D:\software\StandfordNLP\stanford-parser-full-2017-06-09\stanford-parser.jar",
#                             r"D:\software\StandfordNLP\stanford-parser-full-2017-06-09\stanford-parser-3.8.0-models.jar",
#                             r"D:\software\StandfordNLP\stanford-parser-full-2017-06-09\stanford-parser-3.8.0-models"
#                             r"\edu\stanford\nlp\models\lexparser\englishPCFG.ser.gz")
#
# result = eng_parser.parse("I like playing the football.".split())
#
# print(result)
#
# for r in result:
#     print(r)
#     print(r.draw())