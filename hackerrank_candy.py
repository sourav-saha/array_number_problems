## hackerrank: https://www.hackerrank.com/challenges/candies/submissions/code/249835245
'''
It's a classic array preprocessing problm like trapping rain water problem from leetcode, where we need to preprocess the main array 
from left -> right & from right -> left, in order to find out the result.
for explanation check - https://mentorpick.com/blog/view/60f38119f6b44e0e9256e7be
'''



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    # Write your code here
    pa = []
    sa = []
    #fill prefix array
    for i in range(n):
        if i == 0:
            pa.append(1)
        else:
            if arr[i] > arr[i-1]:
                pa.append(1+pa[i-1])
            else:
                pa.append(1)
    
    # fill suffix array
    j = 0   
    for i in reversed(range(n)):
        if i == n-1:
            sa.append(1)
        else:
            if arr[i] > arr[i+1]:
                sa.append(1+sa[j-1])
            else:
                sa.append(1)
        j += 1 
    sa = list(reversed(sa))
    
    res = 0
    for i in range(n):
        res += pa[i] if pa[i] >= sa[i] else sa[i] 
    return res 
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
