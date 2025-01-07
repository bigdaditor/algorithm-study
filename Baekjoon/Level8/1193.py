import sys

input = sys.stdin.readline

n = int(input().rstrip())

line = 0
end = 0

# 라인 수 구하기
while n > end:
    line += 1
    end += line

# 해당 라인에서 끝 수와 차이
diff = end - n

if line % 2 == 0:
    top = line - diff
    bottom = diff + 1
else :
    top = diff + 1
    bottom = line - diff

print(f'{top}/{bottom}')