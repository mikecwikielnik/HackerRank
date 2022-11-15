#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here

    counter = 0

    for _ in range(n):
        y = list(combinations(ar, 2))

    for i in y:
        if sum(i)%k == 0:
            # print(i)
            counter += 1

    x = counter 

    print(x)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
