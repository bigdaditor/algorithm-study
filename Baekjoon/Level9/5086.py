import sys

input = sys.stdin.readline

while True:
    a, b = map(int, input().rstrip().split())
    if a == 0 and b == 0:
        break

    if a < b:
        if b%a == 0:
            print('factor')
        else:
            print('neither')
    else :
        if a%b == 0:
            print('multiple')
        else :
            print('neither')
