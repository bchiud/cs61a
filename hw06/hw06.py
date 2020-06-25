passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

class Fib():
    """A Fibonacci number.
    
    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """
    
    def __init__(self, value=0, prev=0):
        self.value = value
        self.prev = prev
        
    def next(self):
        "*** YOUR CODE HERE ***"
        return Fib(1) if self.value == 0 else Fib(self.value + self.prev, self.value)
        
    def __repr__(self):
        return str(self.value)
        

start = Fib()
start
start.next()
start.next().next()
start.next().next().next()
start.next().next().next()

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price):
        self.balance = 0
        self.item = item
        self.price = price
        self.stock = 0
        
    def vend(self):
        change = self.balance - self.price
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif change < 0:
            return 'You must deposit ${c} more.'.format(c=abs(change))
        elif change == 0:
            self.complete_purchase()
            return 'Here is your {i}.'.format(i=self.item)
        else:
            self.complete_purchase()
            return 'Here is your {i} and ${c} change.'.format(i=self.item, c=change)
            
    def deposit(self, amount):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${a}.'.format(a=amount)
        else:
            self.balance += amount
            return 'Current balance: ${b}'.format(b=self.balance)
    
    def restock(self, amount):
        self.stock += amount
        return 'Current {i} stock: {s}'.format(i=self.item, s=self.stock)
        
    def complete_purchase(self):
        assert self.stock > 0
        assert self.balance >= self.price
        self.balance = 0
        self.stock -= 1
