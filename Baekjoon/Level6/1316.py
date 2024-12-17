import sys
input = sys.stdin.readline

t = int(input().rstrip())

cnt = 0

for _ in range(t):
    string = input().rstrip()
    dictionary = {}
    flag = False

    if len(string) == 1:
        cnt += 1
        continue

    for i in range(len(string)):
        if string[i] in string:
            if dictionary.get(string[i]) is None:
                dictionary[string[i]] = 1
            else :
                if string[i] == string[i-1]:
                    dictionary[string[i]] = dictionary[string[i]]
                else :
                    dictionary[string[i]] = dictionary[string[i]] + 1

    for i in dictionary.values():
        if i > 1:
            flag = False
            break
        else :
            flag = True

    if flag:
        cnt += 1

print(cnt)