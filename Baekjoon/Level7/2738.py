import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n*2)]
sum = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n*2):
    arr[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        sum[i][j] = arr[i][j] + arr[i+n][j]

for i in range(n):
    print(*sum[i])