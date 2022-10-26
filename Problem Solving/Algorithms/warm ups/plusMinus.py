#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos, neg, zero = [], [], []

    for i in arr:
        if i > 0:
            pos.append(i)
        elif i == 0:
            zero.append(i)
        else:
            neg.append(i)

    # not necessary; I just used it to verify the previous for loop
    # print(pos)
    # print(neg)
    # print(zero)
    
    i = len(pos)/len(arr)
    print(f"{i:.6f}")
    j = len(neg)/len(arr)
    print(f"{j:.6f}")
    k = len(zero)/len(arr)
    print(f"{k:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
