#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dict = {}
    ans = 0
    for x in ar:
        t = dict.get(x,0)
        dict[x] = t+1
        if dict[x] % 2 == 0:
            ans += 1
    
    return ans


if __name__ == '__main__':

    # input file
    f = open('input.txt', 'r')
    sys.stdin = f

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
