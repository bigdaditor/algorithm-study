import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())

answer = (a+b)%c
print(answer)

answer = ((a%c) + (b%c))%c
print(answer)

answer = (a*b)%c
print(answer)

answer = ((a%c)*(b%c))%c
print(answer)
