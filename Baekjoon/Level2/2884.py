import sys

H, M = map(int, sys.stdin.readline().rstrip().split())

if M < 45:
    if H == 0:
        H = 24 - 1
    else :
        H = H - 1
    M = (60 + M) - 45
else :
    M = M - 45

print(str(H) + ' ' + str(M))
