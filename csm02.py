def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    if n < 10:
        return True
    if n % 100 // 10 < n % 10:
        return False
    return is_sorted(n // 10)

is_sorted(2)
is_sorted(22222)
is_sorted(9876543210)
is_sorted(9087654321)

def mario_number(level):
    """
    Return the number of ways that Mario can traverse the
    level, where Mario can either hop by one digit or two
    digits each turn. A level is defined as being an integer
    with digits where a 1 is something Mario can step on and 0
    is
    something Mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """
    if level == 1:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        return mario_number(level // 10) + mario_number(level // 100)

mario_number(10101)
mario_number(11101)
mario_number(100101)

def make_change(n):
    """Write a function, make_change that takes in an
    integer amount, n, and returns the minimum number
    of coins we can use to make change for that n,
    using 1-cent, 3-cent, and 4-cent coins.
    Look at the doctests for more examples.
    >>> make_change(5)
    2
    >>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
    2
    """
    if n == 0:
        return 0
    elif n < 3: 
        return 1 + make_change(n -1)
    elif n < 4:
        return 1 + min(make_change(n-1), make_change(n-3))
    else:
        return 1 + min(make_change(n-1), make_change(n-3), make_change(n-4))

make_change(2) # 2
make_change(5) # 2
make_change(6) # 2
make_change(9) # 3
make_change(10) # 3
make_change(11) # 3
make_change(12) # 3



def elephant(name, age, can_fly):
    """
    Takes in a string name, an int age, and a boolean can_fly.
    Constructs an elephant with these attributes.
    >>> dumbo = elephant("Dumbo", 10, True)
    >>> elephant_name(dumbo)
    "Dumbo"
    >>> elephant_age(dumbo)
    10
    >>> elephant_can_fly(dumbo)
    True
    """
    return [name, age, can_fly]

def elephant_name(e):
    return e[0]

def elephant_age(e):
    return e[1]

def elephant_can_fly(e):
    return e[2]

dumbo = elephant("Dumbo", 10, True)
elephant_name(dumbo)
elephant_age(dumbo)
elephant_can_fly(dumbo)




def elephant_roster(elephants):
    """
    Takes in a list of elephants and returns a list of their
    names.
    """
    return [elephant_name(elephant) for elephant in elephants]

dumbo = elephant("Dumbo", 10, True)
dumbo2 = elephant("Dumbo2", 11, False)
elephant_roster([dumbo, dumbo2])


def elephant(name, age, can_fly):
    return [[name, age], can_fly]

def elephant_name(e):
    return e[0][0]

def elephant_age(e):
    return e[0][1]

def elephant_can_fly(e):
    return e[1]

dumbo = elephant("Dumbo", 10, True)
elephant_name(dumbo)
elephant_age(dumbo)
elephant_can_fly(dumbo)



def elephant_roster(elephants):
    """
    Takes in a list of elephants and returns a list of their
    names.
    """
    return [elephant_name(elephant) for elephant in elephants]



def elephant(name, age, can_fly):
    """
    >>> chris = elephant("Chris Martin", 38, False)
    >>> elephant_name(chris)
    "Chris Martin"
    >>> elephant_age(chris)
    38
    >>> elephant_can_fly(chris)
    False
    """
    def select(command):
        if(command == 'name'):
            return name
        elif(command == 'age'):
            return age
        elif(command == 'can_fly'):
            return can_fly
        else:
            return 'Invalid Input'
    return select

def elephant_name(e):
    return e("name")

def elephant_age(e):
    return e("age")

def elephant_can_fly(e):
    return e("can_fly")

dumbo = elephant("Dumbo", 10, True)
elephant_name(dumbo)
elephant_age(dumbo)
elephant_can_fly(dumbo)
