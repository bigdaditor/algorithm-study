import sys

input = sys.stdin.readline

a,b,v = map(int,input().split())

diff = a - b

if v < a:
    print(1)
else :
    if (v-a)%diff == 0:
        print(((v - a) // diff) + 1)
    else :
        print(((v - a) // diff) + 2)