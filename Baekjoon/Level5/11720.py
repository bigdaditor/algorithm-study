import sys
input = sys.stdin.readline

t = int(input().rstrip())
string = input().rstrip()
sum = 0

for i in range(t):
    sum = sum + int(string[i])

print(sum)