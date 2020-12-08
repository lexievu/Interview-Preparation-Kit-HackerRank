#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    matching_pair = 0
    odd_socks = []
    for s in ar:
        if s in odd_socks:
            matching_pair += 1
            odd_socks.remove(s)
        else:
            odd_socks.append(s)
    return matching_pair


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
