#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    d = [0 for i in range(6)] 
    for i in range(6):
        d[i] = arr.count(i)
    print(d)
    x=max(d)    # max takes the first max value in a list (from left to right)
    print(x)
    print(d.index(x))   # this is a neat trick, it calls the index which is the input here

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    #print(result)
