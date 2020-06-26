class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)
        
    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)
        
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