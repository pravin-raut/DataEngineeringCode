arr=[55, 23, 32, 46, 88]

def digitSum(n):
    sum = 0
    while (n):

        sum+=(n%10)
        n=n//10

    return sum


def findMax(arr,n):
    mp={}
    for i in range(n):
        print(arr[i])
        temp=digitSum(arr[i])
        if (temp not in mp):
            mp[temp]=0

        if(mp[temp]!=0):
            if(arr[i])

arr = [55, 23, 32, 46, 88]
n = len(arr)
findMax(arr, n)