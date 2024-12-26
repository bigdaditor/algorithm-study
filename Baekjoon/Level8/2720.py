import sys

input = sys.stdin.readline

t = int(input().rstrip())
tmp = 0
for _ in range(t):
    arr = list()
    n = int(input().rstrip())
    tmp = n
    for i in [25, 10, 5, 1]:
        n = tmp//i
        tmp = tmp%i
        arr.append(n)

    print(*arr)
