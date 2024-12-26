import sys

input = sys.stdin.readline

n = int(input().rstrip())

a = 1
b = 1
idx = 0

if n == 1:
    print(str(a) + '/' + str(b))

for _ in range(n):
    idx += 1
    b += 1
    if a == 1:
        a += 1
        b = 1
    if b == 1:
        a += 1

print(a,b,idx)