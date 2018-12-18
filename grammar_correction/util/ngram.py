# -*- coding:utf-8 -*-

import os

def caculate_probability(sent):
    """
    计算给定文件中每个句子的概率
    :return: 句子的概率值
    """
    tmp_test_file = "tmp_test.txt"
    with open(tmp_test_file, 'w') as f:
        f.write(sent)
    ppl_file = "ppl_test"
    command = predict_command(tmp_test_file, ppl_file=ppl_file)
    os.system(command)
    probps = get_probp(ppl_file=ppl_file)

    return probps

def predict_command(test_file, ppl_file):
    """
    得到计算概率的命令
    :return:
    """
    command = "ngram -ppl {} -order 3 -lm {} -debug 1 > {}".format(test_file, "model.lm", ppl_file)
    return command

def get_probp(ppl_file):
    """
    从ppl结果文件中获取每个句子的概率值
    :return: [pro, ...]
    """
    with open(ppl_file, 'r') as f:
        lines = f.readlines()[2::4]  # 从第三行开始读取，以4为步长
        for line in lines:
            logpt = line.split(" ")[3]
            pp = pow(10, float(logpt))
            return pp

if __name__ == '__main__':
    probps = caculate_probability("It was a surprise entry .")
    print("probps = {}".format(probps))