import sys
input = sys.stdin.readline

arr = list()

for _ in range(10):
    n = int(input())
    n = n%42
    arr.append(n)

arr = set(arr)
print(len(arr))