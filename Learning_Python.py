'''
created on 01.02.2015

@author: владелец
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


max = 0
print(a)
def min(l):
    min = 1000
    for m in l:
        if m < min:
            min = m
    return min

def max(l):
    max = 0
    for g in l:
        if g > max:
            max = g
    return max
def  avg(l):

    sum = 0
    count = 0
    for k in l:
        sum = sum + k
        count = count + 1
    return sum / count

print()
print('min =', min(a),"| max = ", max(a))
print(avg(a))
