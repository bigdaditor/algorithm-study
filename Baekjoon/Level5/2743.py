import sys

input = sys.stdin.readline

string = input().rstrip()
cnt  = 0

for _ in string:
    cnt = cnt + 1

print(cnt)