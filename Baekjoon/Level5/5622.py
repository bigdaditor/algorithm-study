import sys
import string

input = sys.stdin.readline

alpha_list = list(string.ascii_uppercase)
dial_dict = {}
for i in range(len(alpha_list)):
    if alpha_list[i] == 'A' or alpha_list[i] == 'B' or alpha_list[i] == 'C':
        dial_dict[alpha_list[i]] = 2
    if alpha_list[i] == 'D' or alpha_list[i] == 'E' or alpha_list[i] == 'F':
        dial_dict[alpha_list[i]] = 3
    if alpha_list[i] == 'G' or alpha_list[i] == 'H' or alpha_list[i] == 'I':
        dial_dict[alpha_list[i]] = 4
    if alpha_list[i] == 'J' or alpha_list[i] == 'K' or alpha_list[i] == 'L':
        dial_dict[alpha_list[i]] = 5
    if alpha_list[i] == 'M' or alpha_list[i] == 'N' or alpha_list[i] == 'O':
        dial_dict[alpha_list[i]] = 6
    if alpha_list[i] == 'P' or alpha_list[i] == 'Q' or alpha_list[i] == 'R' or alpha_list[i] == 'S':
        dial_dict[alpha_list[i]] = 7
    if alpha_list[i] == 'T' or alpha_list[i] == 'U' or alpha_list[i] == 'V':
        dial_dict[alpha_list[i]] = 8
    if alpha_list[i] == 'W' or alpha_list[i] == 'X' or alpha_list[i] == 'Y' or alpha_list[i] == 'Z':
        dial_dict[alpha_list[i]] = 9

phone_str = input().rstrip()
sum = 0
for char in phone_str:
    duration = 1+dial_dict[char]
    sum += duration

print(sum)