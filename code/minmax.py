
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
# [24, 22, 20, 18, 16]

def miniMaxSum(arr):
    # Write your code here
    nums = []
    for i in range(len(arr)):
        num = 0
        for j in range(len(arr)):
            if i != j:
                num += arr[j]
                
        nums.append(num)

    maxNum= max(nums)
    minNum = min(nums)
    print(minNum, maxNum)

    

if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))

    miniMaxSum([1, 2, 3, 4, 5])






