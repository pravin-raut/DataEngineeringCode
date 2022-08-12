#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    check = all(item in magazine for item in note)
    if check==True:
        print("Yes")
    else:
        print("No")

magazine=['b','a']

magazine.sort()
checkMagazine("two times three is not four","two times two is four")
print(round(1.6))