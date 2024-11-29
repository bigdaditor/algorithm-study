import sys

n1, n2, n3 = map(int, sys.stdin.readline().rstrip().split())
answer = 0

if n1 == n2 and n2 == n3 :
    answer = 10000 + n1 * 1000
elif n1 == n2 or n1 == n3:
    answer = 1000+ n1 * 100
elif n2 == n3:
    answer = 1000 + n2 * 100
else:
    if n1 > n2 and n1 > n3:
        answer = n1 * 100
    if n2 > n3 and n2 > n1:
        answer = n2 * 100
    if n3 > n1 and n3 > n2:
        answer = n3 * 100

print(answer)