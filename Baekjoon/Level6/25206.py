import sys
input = sys.stdin.readline
dictionary = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0,
    'P':0.0
}

sum = 0.0
sum_hakjum = 0.0

for i in range(20):
    class_name,hakjum,grade = input().rstrip().split()
    hakjum = float(hakjum)

    if grade == 'P':
        continue
    else:
        sum = sum + (dictionary[grade]*hakjum)
        sum_hakjum = sum_hakjum + hakjum


print(round((sum/sum_hakjum),6))
