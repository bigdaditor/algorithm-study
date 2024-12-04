import sys
input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    r,s = input().rstrip().split()
    r = int(r)
    p = ''
    for c in s:
        for i in range(r):
            p = p + c
    print(p)