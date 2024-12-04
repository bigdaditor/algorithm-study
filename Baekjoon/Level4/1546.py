import sys

input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
mx = 0

for i in range(n):
    if scores[i] > mx:
        mx = scores[i]

scores = list(map(lambda score : round((score/mx*100),2), scores))
sum = 0

for i in scores:
    sum = sum + i

print(sum/n)