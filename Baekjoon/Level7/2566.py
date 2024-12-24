import sys

input = sys.stdin.readline

arr = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9):
    arr[i] = list(map(int, input().split()))

max = 0
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]
            x = i
            y = j

print(max)
print(x+1, y+1)