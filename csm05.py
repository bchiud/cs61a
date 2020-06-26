class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
        
    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
        
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    Link(1, Link(3))
    >>> a
    Link(1, Link(2, Link(3, Link(4)))) # Original is unchanged
    """
    if lst.rest is Link.empty:
        return Link(lst.first)
    elif lst.rest.rest is Link.empty:
        return Link(lst.first)
    return Link(lst.first, skip(lst.rest.rest))

a = Link(1, Link(2, Link(3, Link(4))))

b = skip(a)
b # Link(1, Link(3))
a # Link(1, Link(2, Link(3, Link(4))))

def skip(lst):
    """
    Mutate original list.
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    None
    >>> a
    Link(1, Link(3))
    """    
    if lst is Link.empty or lst.rest is Link.empty:
        return lst
    lst.rest = lst.rest.rest
    skip(lst.rest)

a = Link(1, Link(2, Link(3, Link(4))))
skip(a)
a # Link(1, Link(3))


def reverse(lst):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> b = reverse(a)
    >>> b
    Link(3, Link(2, Link(1)))
    >>> a
    Link(1, Link(2, Link(3)))
    """
    rev_lst = Link.empty
    while lst is not Link.empty:
        rev_lst = Link(lst.first, rev_lst)
        lst = lst.rest
    return rev_lst

a = Link(1, Link(2, Link(3)))
b = reverse(a)
b # Link(3, Link(2, Link(1)))
a # Link(1, Link(2, Link(3)))


class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches
        
    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches
    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
        
    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])


def contains_n(elem, n, t):
    """
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains(1, 2, t1)
    True
    >>> contains(2, 2, t1)
    False
    >>> contains(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains(1, 3, t2)
    True
    >>> contains(2, 2, t2) # Not on a path
    False
    """
    if n == 0:
        return True
    elif t.is_leaf():
        return t.label == elem and n - 1 == 0
    elif t.label == elem:
        return max([contains_n(elem, n - 1, b) for b in t.branches])
    else:
        return max([contains_n(elem, n, b) for b in t.branches])

t1 = Tree(1, [Tree(1, [Tree(2)])])
contains_n(1, 2, t1) # True
contains_n(2, 2, t1) # False
contains_n(2, 1, t1) # True
t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
contains_n(1, 3, t2) # True
contains_n(2, 2, t2) # False


def factor_tree(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return Tree(n, [factor_tree(i), factor_tree(n // i)])
    return Tree(n)

print(factor_tree(20))