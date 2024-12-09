import sys
input = sys.stdin.readline

str1, str2 = input().rstrip().split()

num1, num2 = '', ''
for i in range(3,0,-1):
    num1 = num1 + str1[i-1]
    num2 = num2 + str2[i-1]

num1, num2 = int(num1), int(num2)

if num1 > num2:
    print(num1)
else:
    print(num2)