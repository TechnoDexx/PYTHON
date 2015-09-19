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


def function_testing(one, two):
    one = addval(one, 0)
    print('a =', one)
    two = addval(two, 0)
    print('b =', two)
    print()
    print('min(a) =', minimum(one), "| max(a) = ", maximum(one))
    print('average(a) =', avg(one))
    print()
    print('min(b) =', minimum(two), "| max(b) = ", maximum(two))
    print('average(b) =', avg(two))
    print()
    print('intercept(a,b) =', intercept(one, two), '\n')
    print('sum(a) =', sum(one), '| sum(b) =', sum(two))
    return
