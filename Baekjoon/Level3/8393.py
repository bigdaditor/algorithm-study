import sys
input = sys.stdin.readline

n = int(input().rstrip())
sum = 0

for i in range(n):
    sum = sum + (i+1)

print(sum)
