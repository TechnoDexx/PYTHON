"""
created on 01.02.2015

@author: владелец
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

json = ""


def addval(l, value):
    l = set(l)
    res = []
    for i in l:
        res.append(i + value)
    return res


def intercept(x, y):
    x = set(x)
    y = set(y)
    res = []
    for i in y:
        if i in x:
            res.append(i)
    return res


def minimum(l):
    _min = 1000
    for m in l:
        if m < _min:
            _min = m
    return _min


def maximum(l):
    _max = 0
    for g in l:
        if g > _max:
            _max = g
    return _max


def avg(l):
    count = 0
    for _ in l:
        count += 1
    return sum(l) / count


def function_testing(first_list, second_list,  addingvalue_one=0, addingvalue_two=0):
    first_list = addval(first_list, addingvalue_one)
    second_list = addval(second_list, addingvalue_two)

    print()
    print('a =', first_list)
    print('b =', second_list)
    print()
    print('min(a) =', minimum(first_list), "| max(a) = ", maximum(first_list))
    print()
    print('average(a) =', avg(first_list))
    print()
    print('min(b) =', minimum(second_list), "| max(b) = ", maximum(second_list))

    print('average(b) =', avg(second_list))
    print()
    print('intercept(a,b) =', intercept(first_list, second_list), '\n')
    print('sum(a) =', sum(first_list), '| sum(b) =', sum(second_list))
    return


function_testing(a, b, 3, 4)

