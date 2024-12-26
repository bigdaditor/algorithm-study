import sys

input = sys.stdin.readline

n = int(input().rstrip())

if n == 1:
    print(1)
    exit()

a = 1
l = 2
while True:
    # l == 2
    mx = 6 * a + 1
    if n <= mx:
        print(l)
        break
    a += l
    l += 1

