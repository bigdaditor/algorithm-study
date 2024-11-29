import sys
input = sys.stdin.readline

n = int(input().rstrip())
n = int(n/4)

long_str = ""

for _ in range(n):
    long_str = long_str + "long "

print(long_str+"int")