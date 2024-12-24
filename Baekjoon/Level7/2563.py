import sys
input = sys.stdin.readline

n = int(input().rstrip())
canvas = [[0 for i in range(100)] for j in range(100)]

for i in range(n):
    x, y = map(int, input().rstrip().split())

    for j in range(x, x+10):
        for k in range(y, y+10):
            canvas[j][k] = 1

sum = 0
for i in range(100):
    for j in range(100):
        if canvas[i][j] == 1:
            sum += 1

print(sum)