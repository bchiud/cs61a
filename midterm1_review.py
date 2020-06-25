from operator import add, mul, pow

def mystery(f, x):
    """
    >>> from operator import add, mul
    >>> a = mystery(add, 3)
    >>> a(4) # add(3, 4)
    7
    >>> a(12)
    15
    >>> b = mystery(mul, 5)
    >>> b(7) # mul(5, 7)
    35
    >>> b(1)
    5
    >>> c = mystery(lambda x, y: x * x + y, 4)
    >>> c(5)
    21
    >>> c(7)
    23
    """
    return lambda y: f(x,y)

def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        if k == 1:
            return middle
        return middle + '-' + repeat(k - 1)
    return start + '-' + repeat(num) + '-' + end

(lambda x: lambda y: ________________)(_____)(lambda z: z*z)()

(lambda x: lambda y: lambda: y(x))(3)(lambda z: z*z)()




def make_alternator(f, g):
    """
    >>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
    >>> a(5)
    1
    6
    9
    8
    25
    """
    def printer(n):
        i = 1
        while i <= n:
            print(f(i) if i % 2 else g(i))
            i += 1
    return printer


Implement replace, which takes in a number n, a digit old and a digit new,
and returns a number identical to n, but where every occurrence of the digit
old is replaced with the digit new.




def replace(n, old, new):



    if n % 10


def replace(n, old, new):
    def replacer(x):
        return new if x == old else x
    if n < 10:
        return replacer(n)
    return str(replace(n // 10, old, new)) + str(replacer(n % 10))


def stairs(n):
    """
    >>> stairs(5)
    13
    >>> stairs(10)
    274
    """
    if(n < 0):
        return 0
    elif(n == 0):
        return 1
    return stairs(n-1) + stairs(n-2) + stairs(n-3)

def stairs(n, k):
    """
    >>> stairs(5, 2)
    8
    >>> stairs(5, 5)
    16
    >>> stairs(10, 5)
    464
    """
    if(n < 0):
        return 0
    elif(n == 0):
        return 1
    steps = 1
    ways = 0
    while steps <= k:
        ways += stairs(n - steps, k)
        steps += 1
    return ways



Implement the memory function, which takes a number x and a singleargument function f. It returns a function with a peculiar behavior that
you must discover from the doctests. You may only use names and call
expressions in your solution. You may not write numbers or use
features of Python not yet covered in the course.


square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
    """Return a higher-order function that prints its memories.
    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    def helper(new_func):
        print(f(x))
        return memory(x, new_func)
    return helper


def counter(base):
    """Return a function which accepts digits in a given base and returns the value in base
    10 after encountering 'done'. Numbers that are not digits in the given base are ignored.
    >>> binary = counter(2)
    >>> binary('done')
    0
    >>> binary(1)(0)(1)(1)('done') # see example above
    11
    >>> binary(1)(2)(3)(0)(1)('done') # 2 and 3 are not digits in base 2
    5
    >>> quaternary = counter(4)
    >>> quaternary(1)(2)(3)(0)(1)('done') # 1*(4**4) + 2*(4**3) + 3*(4**2) + 0*(4**1) + 1*1
    433
    """
    def helper(digit, total):
        if digit == 'done':
            return total
        if digit >= base:
            return lambda x: helper(x, total)
        else:
            return lambda x: helper(x, total * base + digit)
    return lambda x: helper(x, 0)     


def combine(n, f, result):
    """
    Combine the digits in non-negative integer n using f.
    >>> combine(3, mul, 2) # mul(3, 2)
    6
    >>> combine(43, mul, 2) # mul(4, mul(3, 2))
    24
    >>> combine(6502, add, 3) # add(6, add(5, add(0, add(2, 3)
    )))
    16
    >>> combine(239, pow, 0) # pow(2, pow(3, pow(9, 0))))
    8
    """
    if n == 0:
        return result
    else:
        return combine(n // 10 , f , f(n % 10, result))

def has_sum(total, n, m):
    """
    >>> has_sum(1, 3, 5)
    False
    >>> has_sum(5, 3, 5) # 0 * 3 + 1 * 5 = 5
    True
    >>> has_sum(11, 3, 5) # 2 * 3 + 1 * 5 = 11
    True
    """
    if total < 0:
        return False
    if total == 0:
        return True
    return has_sum(total - n, n, m) or has_sum(total - m, n, m)

def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer 1 prints within this range
    True
    >>> sum_range(40, 55) # Printer 1 can print a number 56-60
    False
    >>> sum_range(170, 201) # Printer 1 + 2 will print between
    180 and 200 copies total
    True
    """
    if lower < 0 or upper < 0:
        return False
    if lower <= 130 and upper >= 140:
        return True
    if lower <= 50 and upper >= 60:
        return True
    return sum_range(lower - 50, upper - 60) or sum_range(lower - 130, upper - 140)



def parabola(x):
    """A parabola function (for testing the again function)."""
    return (x-3) * (x-6)

def vee(x):
    """A V-shaped function (for testing the again function)."""
    return abs(x-2)

def again(f):
    """Return the smallest non-negative integer n such that f(n) == f(m) for some m < n.
    >>> again(parabola) # parabola(4) == parabola(5)
    5
    >>> again(vee) # vee(1) == vee(3)
    3
    """
    n = 1
    while True:
        m = 0
        while m < n:
            if f(n) == f(m):
                return n
            m += 1
        n = n + 1


# Definition. Two adjacent digits in a non-negative integer are an increase if the left digit is smaller than the
# right digit, and a decrease if the left digit is larger than the right digit.
# For example, 61127 has 2 increases (1 → 2 and 2 → 7) and 1 decrease (6 → 1).
# You may use the sign function defined below in all parts of this question.
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# (5 pt) Implement ramp, which takes a non-negative integer n and returns whether it has more increases
# than decreases when reading its digits from left to right (see the definition above).
def ramp(n):
"""Return whether non-negative integer N has more increases than decreases.
>>> ramp(123) # 2 increases (1 -> 2, 2 -> 3) and 0 decreases
True
>>> ramp(1315) # 2 increases (1 -> 3, 1 -> 5) and 1 decrease (3 -> 1)
True
>>> ramp(176) # 1 increase (1 -> 7) and 1 decrease (7 -> 6)
False
>>> ramp(5) # 0 increases and 0 decreases
False
"""
    n, last, tally = n // 10, n % 10, 0
    while n:
        n, last, tally = n // 10, n % 10, tally + sign(last - n % 10)
    return tally > 0

# (3 pt) Implement over_under, which takes a number y and returns a function that takes a number x.
# This function returns 1 if x is greater than y, 0 if x equals y, and -1 if x is less than y.
# You may not use if, and, or or.
def over_under(y):
    """Return a function that takes X and returns:
    -1 if X is less than Y
    0 if X is equal to Y
    1 if X is greater than Y
    >>> over_under(5)(3) # 3 < 5
    -1
    >>> over_under(5)(5) # 5 == 5
    0
    >>> over_under(5)(7) # 7 > 5
    1
    """
    return lambda x: sign(x - y)


# Read this first. The process function below uses tally and result functions to analyze all adjacent
# pairs of digits in a non-negative integer n. A tally function is called on each pair of adjacent digits.
def process(n, tally, result):
    """Process all pairs of adjacent digits in N using functions TALLY and RESULT."""
    while n >= 10:
        tally, result = tally(n % 100 // 10, n % 10)
        n = n // 10
    return result()

# (c) (6 pt) Implement ups, which returns two functions that can be passed as tally and result arguments
# to process, so that process computes whether a non-negative integer n has exactly k increases.
# Hint: You can use sign from the previous page and the built-in max and min functions.
def ups(k):
    """Return tally and result functions that compute whether N has exactly K increases.
    >>> f, g = ups(3)
    >>> process(1200849, f, g) # Exactly 3 increases: 1 -> 2, 0 -> 8, 4 -> 9
    True
    >>> process(94004, f, g) # 1 increase: 0 -> 4
    False
    >>> process(122333445, f, g) # 4 increases: 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
    False
    >>> process(0, f, g) # 0 increases
    False
    """
    def f(left, right):
        return ups(k - max(sign(right - left), 0))
    return f, lambda: k == 0

f, g = ups(3)
process(1200849, f, g)
process(94004, f, g)
process(122333445, f, g)
process(0, f, g)



# (3 pt) Implement at_most, which returns True if the number of increases in a non-negative integer n is
# less than or equal to k, and False otherwise. Assume ups is implemented correctly. You may use any of
# the functions from previous parts of this question: sign, ramp, over_under, and process.
def at_most(n, k):
    """Return whether non-negative integer N has at most K increases.
    >>> at_most(567, 3)
    True
    >>> at_most(567, 2)
    True
    >>> at_most(567, 1)
    False
    """
    result = False
    while k >= 0:
        a, b = ups(k) # tally(), result 
        k, result = k - 1, result or process(n, a, b) 
    return result

at_most(567, 3)
at_most(567, 2)
at_most(567, 1)
