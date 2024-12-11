import sys

input = sys.stdin.readline
string = input().rstrip()

def count_croatia_alpha(string):
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    cnt = 0
    for c in croatia:
        if c in string:
            cnt += 1
            string = string.replace(c, '')
        else :

            count_croatia_alpha(string)
    if string == '':
        return cnt

