#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # Begin by sorting the list in ascending order
    arr.sort()

    # Find minimum sum by summing the first 4 elements
    minimum = sum(arr[:4])
    # Find maximum sum by summing the last 4 elements of the list
    maximum = sum(arr[-4:])


    print(f"{minimum} {maximum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
