import sys
input = sys.stdin.readline

n = int(input())
line = 2*n-1
for _ in range(line):
    blank = ''
    star = ''
    for i in range(n):
        for j in range(n-1-i):
            blank = blank + ' '
        for k in range(i):
            star = star + '*'
        print(star)