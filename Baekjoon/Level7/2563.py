import sys
input = sys.stdin.readline

n = int(input().rstrip())
square = [[0 for _ in range(4)] for _ in range(n)]

for i in range(n):
    x, y = map(int, input().rstrip().split())
    square[i][0] = x
    square[i][1] = y
    square[i][2] = x+10
    square[i][3] = y+10

print(square)
