#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here

    # remove the item anna didn't eat
    bill.pop(k)
    # print(bill)     # checkpoint

    # find the avg of the *true* bill
    sum_bill = sum(bill)
    # print(sum_bill)
    avg_bill = sum_bill/2

    if avg_bill == b:
        print("Bon Appetit")
    else:
        x = abs(avg_bill - b)
        print(round(x))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())    # the amount charged to anna, the third line of input // user input

    bonAppetit(bill, k, b)