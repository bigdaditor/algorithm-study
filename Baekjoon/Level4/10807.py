import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
find = int(input().rstrip())
count = 0

for i in range(n):
    if arr[i] == find:
        count += 1

print(count)