import sys

input = sys.stdin.readline

t = int(input().rstrip())
cnt = 0
answer = ''

for _ in range(t):
    string = input().rstrip()
    if len(string) == 1:
        print(string+string)
    else:
        print(string[0]+string[len(string)-1])