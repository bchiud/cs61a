def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

t = tree(1,
    [tree(3,
        [tree(4),
        tree(5),
        tree(6)]),
    tree(2)])


def tree_max(t):
    """Return the max of a tree."""
    return max([label(t)] + [tree_max(b) for b in branches(t)])

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    return 1 + max(height(b) for b in branches(t))

def square_tree(t):
    """Return a tree with the square of every element in t"""
    return [label(t) ** 2] + [square_tree(b) for b in branches(t)]

numbers = tree(1,
    [tree(2,
        [tree(3),
        tree(4)]),
    tree(5,
        [tree(6,
            [tree(7)]),
        tree(8)])])
print_tree(square_tree(numbers))


def find_path(tree, x):
    """
    >>>  t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path

t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
find_path(t, 5)
find_path(t, 10)