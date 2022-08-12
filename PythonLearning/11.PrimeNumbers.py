TotalInput=100

def PrimeNumberCheck(num):
    if num<2:
        return 0
    primeList=[2]
    Count=3
    print(primeList)
    for y in primeList:
        if Count%y==0:
           Count += 2
           break
        else:
            primeList.append(Count)
            Count += 2
    

PrimeNumberCheck(100)
