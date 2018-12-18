#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from grammar_correction.rpc_model.demo_thrift.format_data import Client
from grammar_correction.rpc_model.demo_thrift.format_data import Data

sys.path.append('..')


def rpc_correct(src):
    """
    调用远程的model进行语法纠错
    :param src: 原始语句
    :return: 改正后语句
    """
    __HOST = '10.117.62.105'
    __PORT = 8888

    tsocket = TSocket.TSocket(__HOST, __PORT)
    transport = TTransport.TBufferedTransport(tsocket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Client(protocol)

    data = Data(src)
    transport.open()

    result = client.do_format(data).text

    print("grammar backend correct result = {}".format(result))

    return result

if __name__ == '__main__':
    # __HOST = 'localhost'
    #__HOST = '10.108.138.114'
    __HOST = '10.117.62.105'
    __PORT = 8888

    tsocket = TSocket.TSocket(__HOST, __PORT)
    transport = TTransport.TBufferedTransport(tsocket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Client(protocol)

    data = Data('hello,world!')
    transport.open()

    print(client.do_format(data).text)
