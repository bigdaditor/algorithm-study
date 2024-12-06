import sys

arr = list(map(int, sys.stdin.readline().split()))
chess = [1,1,2,2,2,8]
answer = []

for i in range(len(arr)):
    answer.append(chess[i] - arr[i])

print(*answer)