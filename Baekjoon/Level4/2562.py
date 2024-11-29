import sys
input = sys.stdin.readline

mx = 0
idx = 0
for i in range(9):
    n = int(input().rstrip())
    if mx < n:
        mx = n
        idx = i+1

print(mx)
print(idx)

