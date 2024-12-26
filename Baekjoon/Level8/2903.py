import sys

input = sys.stdin.readline

n = int(input().rstrip())
d = (2**n)+1
print(d*d)