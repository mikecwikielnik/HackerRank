#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    # notice no list being used here! 

    high_score = -1
    low_score = 100000001

    high_score_count = 0
    low_score_count = 0

    for i in scores:
        if i > high_score:
           high_score = i
           high_score_count += 1
        if i < low_score:
            low_score = i
            low_score_count += 1
    # print(high_score)
    a = high_score_count - 1
    # print(low_score)
    b = low_score_count - 1

    # print final results
    print(f"{a} {b}")
if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
