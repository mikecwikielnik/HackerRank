#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here

    dict = Counter(ar)
    # print(dict)
    pairs = 0

    for k, v in dict.items():
        if v%2 == 0:
            x = v/2
            pairs += x
        elif v%2 != 0:
            if v == 1:
                pass
            elif v != 1:
                k = (v-1)
                k = k/2
                pairs += k
            else:
                x = v%2
                pairs += x
             
    print(round(pairs))

if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)