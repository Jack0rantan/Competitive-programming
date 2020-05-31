#!/bin/python3

import sys

f = open('input.txt','r')
input = f.readline

S = input().strip()

try:
    print(int(S))
except ValueError:
    print('Bad String')

