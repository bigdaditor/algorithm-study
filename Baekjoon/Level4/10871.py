import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
answer = list()

for i in range(n):
    if arr[i] < x:
        answer.append(arr[i])

print(*answer)