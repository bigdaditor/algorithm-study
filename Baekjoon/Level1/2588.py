import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
# 1의 자리
one = b%10
# 10의 자리
ten = int(((b%100)-one)/10)
# 100의 자리
hundred = int(b/100)

print(a*one)
print(a*ten)
print(a*hundred)
print(a*b)
