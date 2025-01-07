import math
import sys

input = sys.stdin.readline

a,b,v = map(int,input().split())

diff = a - b

print(v/diff)