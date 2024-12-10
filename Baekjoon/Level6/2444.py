import sys
input = sys.stdin.readline

n = int(input())
line = 2*n-1

for i in range(line):
    # 별 찍기 라인
    idx = i + 1
    blank = ''
    star = ''

    # 입력된 수보다 작을 때는 인덱스
    if idx < n:
        blank_idx = n - idx
        star_idx = idx
    else:
        blank_idx = idx - n
        star_idx = n-blank_idx

    for j in range(blank_idx):
        blank = blank + ' '
    for k in range(star_idx):
        # 첫 줄과 마지막 줄은 하나만 추가
        if k == 0 or k == line:
            star = star + '*'
        else :
            star = star + '**'

    print(blank + star)