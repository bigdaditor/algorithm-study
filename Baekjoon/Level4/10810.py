import sys
input = sys.stdin.readline

# n : 바구니 갯수, m: 공을 넣을 횟수
n, m = map(int, input().rstrip().split())
basket = []

for i in range(n):
    basket.append(0)

for _ in range(m):
    s,e,num = map(int, input().rstrip().split())
    s = s-1
    for i in range(s,e):
        basket[i] = num

print(*basket)