#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    l=[]
    length=len(arr)
    First=int(length/2)
    FirstList=arr[0:First]

    FirstOp=round(sum(FirstList)/len(FirstList))

    if len(arr)%2!=0:
        SecondList=arr[First]
        #print(SecondList)
        SecondOp = SecondList

    else:
        #print("Inside")
        SecondList=arr[First-1:First+1]
        #print('{0:.0f}'.format(sum(SecondList)/len(SecondList)))
        SecondOp = round(sum(SecondList) / len(SecondList))
    if len(arr)%2!=0:
        ThirdList=arr[First+1:]
        print(ThirdList)
        #print('{0:.0f}'.format(sum(ThirdList)/len(ThirdList)))
        ThirdOp = round(sum(ThirdList) / len(ThirdList))

    else:
        ThirdList = arr[First:]
        print(ThirdList)
        #print('{0:.0f}'.format(sum(ThirdList) / len(ThirdList)))
        ThirdOp = round(sum(ThirdList) / len(ThirdList))

    l.append(FirstOp)
    l.append(SecondOp)
    l.append(ThirdOp)
    return l

if __name__ == '__main__':

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)
    print(res)

#10
#3 7 8 5 12 14 21 15 18 14