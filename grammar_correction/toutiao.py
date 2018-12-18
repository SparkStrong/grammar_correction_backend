# -*- coding:utf-8 -*-

import sys

def main():
    n = 8
    flag_list = [sys.maxsize]
    res = count_num(n, 1, 1, 0, flag_list)

    return res

def count_num(n, a, b, count, flag_list):
    if n < a + b:
        return sys.maxsize

    if a * 2 == n:
        return count + 1
    elif a + b == n:
        return count + 1
    else:
        countOne = count_num(n, a*2, a, count+1, flag_list)
        countTwo = count_num(n, a+b, b, count+1, flag_list)

        min1 = min(countOne, countTwo)
        flag_list[0] = min(min1, flag_list[0])

        return flag_list[0]

if __name__ == '__main__':
    res = main()
    print(res)