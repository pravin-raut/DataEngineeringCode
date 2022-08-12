from random import *

def shufflelist(inputlist):
    shuffle(inputlist)
    return inputlist

def UserInput():
    inputvalue = input("Please give input between 1 to 3 {}")
    return int(inputvalue)

def validateGuess(sl):
    User=UserInput()-1
    shufflelist(sl)
    print(sl)
    if(User==sl.index('0')):
        print("Correct Gueess")
    else:
        print("Incorrect Guess")
        validateGuess(sl)

mylist=['','0','']
validateGuess(mylist)
