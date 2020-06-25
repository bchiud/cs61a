""" Optional problems for Lab 6 """

## Nonlocal practice
def vending_machine(snacks):
    """Cycles through sequence of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    index = 0
    def dispense():
        nonlocal index
        return_snack = snacks[index]
        index = ( index + 1 ) % len(snacks)
        return return_snack
    return dispense


vender = vending_machine(('chips', 'chocolate', 'popcorn'))
vender()
vender()
vender()
vender()
other = vending_machine(('brownie',))
other()