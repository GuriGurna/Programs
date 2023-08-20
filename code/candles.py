#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    numbers=0
    maxheight = max(candles)
    for i in candles:
        if i == maxheight:
            numbers += 1
    print(numbers)   


birthdayCakeCandles([5,3,6,2,6,6])