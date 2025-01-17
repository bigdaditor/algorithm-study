import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

factor = list()

for i in range(1, n+1):
    if n % i == 0:
        factor.append(i)

if len(factor) < k:
    print(0)
else :
    print(factor[k-1])