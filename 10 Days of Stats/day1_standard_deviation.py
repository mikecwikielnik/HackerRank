#!/bin/python3


import math
import os
import random
import re
import sys



#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function

    # find the mean
    sum_mean = sum(arr)
    mean = sum_mean/len(arr)

    # subtract the mean from each element
    for i in range(len(arr)):
        arr[i] = arr[i] - mean
        
    # print(arr)


    # square all elements in list
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2
        
    # print(arr)

    # # add up all elements in list
    sum_arr = sum(arr)
    # print(sum_arr)
        
    # divide the terms in list aka the average lol
    average = sum_arr/len(arr)
    # print(average)

    # square root
    sqrt_arr = math.sqrt(average)   # math class! 

    # round
    sqrt_arr = round(sqrt_arr, 1)
    print(sqrt_arr)
    # print(type(sqrt_arr))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)


