def stepper(num):
    def step():
        nonlocal num
        num = num + 1
        return num
    return step

s = stepper(3)
s()
s()

def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def helper(f):
        nonlocal n
        n = f(n)
        print(n)
        return helper
    return helper

f = memory(10)
f = f(lambda x: x * 2)
f = f(lambda x: x - 7)
f = f(lambda x: x > 5)



def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    xs = [i for i in lst if i == x]
    for _ in xs:
        lst.append(el)

def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    l = len(lst)
    for i in [x for x in range(-2, -len(lst) - 1, -1)]:
        lst.append(lst.pop(i))

x = [3, 2, 4, 5, 1]
reverse(x)
x


def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    d = {}
    for p in s:
        fnp = fn(p)
        if fnp in d:
            d[fnp].append(p)
        else:
            d[fnp] = [p]
    return d

group_by([12, 23, 14, 45], lambda p: p // 10)
group_by(range(-3, 4), lambda x: x * x)


def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for k,v in d.items():
        if type(v) == dict:
            replace_all_deep(v, x, y)
        elif v == x:
            d[k] = y

d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
replace_all_deep(d, 'x', 'y')
d
