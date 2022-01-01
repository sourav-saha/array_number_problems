##  Hackerrank problem link:
## https://www.hackerrank.com/contests/being-zero/challenges/recursive-digit-sum/problem



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    init_sum = s * k
    
    while True:
        if init_sum < 10:
            return init_sum
        else:
            s = 0
            while init_sum > 0:
                s += init_sum%10
                init_sum = init_sum // 10
            init_sum = s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
