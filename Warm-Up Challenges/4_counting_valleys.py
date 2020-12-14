#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
# Valley: step down from sea level, end with a step up to sea level


def countingValleys(steps, path):
    no_of_valleys = 0
    level = 0 # 0 is sea level, negative values are below sea level, positive values are above sea level
    step_down = False
    step_up = False
    for i in range(steps):
        if path[i] == 'D':
            if level == 0:
                step_down = True
            level -= 1
        else: # if steps[i] == 'U'
            if level == -1:
                step_up = True
            level += 1
        if step_up and step_down:
            no_of_valleys += 1
            step_up = False
            step_down = False
    return no_of_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
