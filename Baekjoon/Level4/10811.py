import sys
input = sys.stdin.readline

n, m = map(int, input().split())

basket = list()

for i in range(n):
    basket.append(i+1)

for _ in range(m):
    s, e = map(int, input().split())
    s, e = s-1, e-1
    mid = (e-s)//2
    for i in range(mid+1):
        left, right = s+i, e-i
        if left == right:
            continue
        temp = basket[left]
        basket[left] = basket[right]
        basket[right] = temp

print(*basket)
