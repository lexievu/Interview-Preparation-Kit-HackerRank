#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1, -1, -1):
        if (q[i] - (i + 1) > 2):  # if the person bribes more than 2 people
            print("Too chaotic")
            return None
        else:
            for j in range(max(0, q[i] - 2), i):
                if q[j] > q[i]:
                    bribes += 1
    print(bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
