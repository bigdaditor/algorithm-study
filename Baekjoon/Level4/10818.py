import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

mn = arr[0]

if n == 1:
    mx = arr[0]
else :
    mx = arr[1]

if mn > mx:
    mx = mn
    mn = mx

if n > 2:
    for i in range(n):
        current = arr[i]
        if current < mn:
            mn = current
        if current > mx:
            mx = current

print(mn,mx)