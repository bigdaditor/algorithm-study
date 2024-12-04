import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
basket = list()

# 바구니에 번호별 공 넣어서 초기화
for i in range(n):
    basket.append(i+1)

for i in range(m):
    s,e = map(int, input().rstrip().split())
    s = s-1
    e = e-1
    tmpS = basket[s]
    tmpE = basket[e]
    basket[e] = tmpS
    basket[s] = tmpE

print(*basket)