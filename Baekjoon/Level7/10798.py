import sys

input = sys.stdin.readline
arr = [['*' for _ in range(15)] for _ in range(5)]

for i in range(5):
    ele = input().rstrip()
    for j in range(len(ele)):
        arr[i][j] = ele[j]

string = ''
for j in range(15):
    for i in range(5):
        if arr[i][j] == '*':
            continue
        string += arr[i][j]

print(string)