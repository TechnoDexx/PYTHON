"""
created on 01.02.2015

@author: владелец
"""

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [10, 11, 12, 13, 14, 15, 16]


def addval(l, value):
    res = []
    for i in l:
        res.append(i + value)
    return res


def intercept(x, y):
    x = set(x)
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
    _sum = 0
    count = 0
    for k in l:
        _sum = _sum + k
        count += 1
    return _sum / count


a = addval(a, 3)
print('a =', a)
b = addval(b, -3)
print('b =', b)
print()
print('min(a) =', minimum(a), "| max(a) = ", maximum(a))
print('average(a) =', avg(a))
print()
print('min(b) =', minimum(b), "| max(b) = ", maximum(b))
print('average(b) =', avg(b))
print()
print('intercept(a,b) =', intercept(a, b), '\n')
print('sum(a) =', sum(a), '| sum(b) =', sum(b))
