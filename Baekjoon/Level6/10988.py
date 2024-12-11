import sys

input = sys.stdin.readline
string = input().rstrip()
string = list(string)
mid = len(string) // 2
cnt = 0

for i in range(mid):
    right = string[len(string)-1-i]
    left = string[i]

    if left == right:
        cnt = cnt+1

if cnt == mid:
    print(1)
else :
    print(0)