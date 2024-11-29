import sys
input = sys.stdin.readline

n = int(input().rstrip())
star = ''
space = ''

for i in range(n):
    space = ''
    for j in range(n-i-1):
        space = space + ' '
    star = star + '*'
    print(space+star)
