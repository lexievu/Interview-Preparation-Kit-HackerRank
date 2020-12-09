#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    no_of_a = 0
    s_a = 0
    for i in s:
        if i == 'a':
            s_a += 1

    no_of_a = s_a * (n // len(s))

    for i in range(n % len(s)):
        if s[i] == "a":
            no_of_a += 1

    return no_of_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
