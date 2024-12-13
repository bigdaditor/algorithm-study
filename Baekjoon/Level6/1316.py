import sys
input = sys.stdin.readline

t = int(input().rstrip())
list = []
cnt = 0

for _ in range(t):
    string = input().rstrip()
    flag = False

    if len(string) == 1:
        cnt += 1
        continue

    for i in range(len(string)):
        if i < len(string)-1:
            if string[i] == string[i+1]:
                flag = True
                list.append(string[i])
            else :
                if string[i] in list:
                    flag = False
                else:
                    flag = True
                    list.append(string[i])
        else:
            if string[i] in list:
                flag = False
            else:
                flag = True
                list.append(string[i])

    if flag:
        cnt += 1

print(cnt)