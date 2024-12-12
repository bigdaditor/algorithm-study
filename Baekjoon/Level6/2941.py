import sys

input = sys.stdin.readline
string = input().rstrip()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in croatia:
    if c in string:
        string = string.replace(c, '/')

print(len(string))
