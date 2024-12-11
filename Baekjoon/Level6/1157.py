import sys

input = sys.stdin.readline
string = input().rstrip().lower()
string = list(string)
dictionary = {}

for char in string:
    if char not in dictionary:
        dictionary[char] = dictionary.get(char, 0) + 1
    else :
        dictionary[char] = dictionary[char] + 1

max = 0
cnt = 0
for key, value in dictionary.items():
    if value > max:
        max = value

for key, value in dictionary.items():
    if value == max:
        cnt += 1

if cnt > 1:
    print('?')
else :
    for key, value in dictionary.items():
        if value == max:
            print(str(key).upper())
            break