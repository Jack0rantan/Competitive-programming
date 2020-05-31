#!/bin/python3

import math
import os
import random
import re
import sys

f = open('input.txt','r')
input = f.readline


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    count = 0
    for i in arr:
        if i == []:
            count += 1
    for i in range(count):
        arr.remove([])

    res = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if 0 <= i-1 and i+1 < len(arr) and 0 <= j-1 and j+1 < len(arr[i]):
                res.append(sum(arr[i-1][j-1:j+2]) + arr[i][j] + sum(arr[i+1][j-1:j+2]))
    print(max(res))
    