import sys

input = sys.stdin.readline

while True:
    n = int(input().rstrip())

    if n == -1:
        break

    sum = 0
    arr = list()
    for i in range(1,n+1):
        if n % i == 0 and i != n:
            sum = sum + i
            arr.append(i)

    if n == sum:
        string = str(n) + ' = '
        for i in arr:
            if i == arr[len(arr)-1]:
                string = string + str(i)
            else :
                string = string + str(i) + ' + '
    else :
        string = str(n) + ' is NOT perfect.'

    print(string)