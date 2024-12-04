import sys
input = sys.stdin.readline

arr = list()

for i in range(30):
    arr.append(0)

for i in range(28):
    ok = int(input())
    arr[ok-1] = ok

for i in range(len(arr)):
    if arr[i] == 0:
        print(i+1)