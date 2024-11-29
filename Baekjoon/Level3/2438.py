import sys
input = sys.stdin.readline

n = int(input().rstrip())
star = ''

for i in range(n):
    star = star + '*'
    print(star)