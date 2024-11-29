import sys
input = sys.stdin.readline

x = int(input().rstrip())
n = int(input().rstrip())
sum = 0

for _ in range(n):
    a, b = map(int, input().rstrip().split())
    sum = sum + (a*b)

if sum == x:
    print("Yes")
else:
    print("No")