import sys

# H: 시 M: 분
H, M = map(int, sys.stdin.readline().rstrip().split())
# a: 요리시간
a = int(sys.stdin.readline().rstrip())
# cook_hour: 요리시간과 분을 더해 60으로 나눈 시간
# cook_min: 요리시간과 분을 더해 60으로 나눈 분
cook_hour = int((M+a)/60)
cook_min = int((M+a)%60)


if M + a >= 60:
    H = H + cook_hour
    if H >= 24:
        H = H-24
    M = cook_min
else:
    M = M + a

print(H,M)