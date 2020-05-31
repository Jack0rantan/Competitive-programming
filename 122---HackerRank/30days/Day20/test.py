#!/bin/python3

import sys

input = open('input.txt','r').readline

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

# Track number of elements swapped during a single array traversal
numberOfSwaps = 0
for i in range(n):

    for j in range(n-1):
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            numberOfSwaps = numberOfSwaps + 1
    
    # If no elements were swapped during a traversal, array is sorted
    if numberOfSwaps == 0:
        break

print('Array is sorted in {} swaps.'.format(numberOfSwaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))