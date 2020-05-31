#!/bin/python3

import math
import os
import random
import re
import sys

f = open('input.txt','r')
input = f.readline

if __name__ == '__main__':
    n = int(input())
    ss = bin(n)[2:].split('0')
    ans = 0
    for i in ss:
        if ans < len(i):
            ans = len(i)
    print(ans)