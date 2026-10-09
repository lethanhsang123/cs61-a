from tree import Tree, is_leaf


def sum_leaves(t: Tree[int]) -> int:
    """Return the sum of the labels of the leaves of tree t

    >>> t = Tree(3, [Tree(4), Tree(5, [Tree(6), Tree(7)])])
    >>> sum_leaves(t) # 4 + 6 + 7
    17
    """
    if is_leaf(t):
        return t.label
    return sum([sum_leaves(l) for l in t.branches])


def largest_leaf[T](t: Tree[T]) -> T:
    """Return the largest label of the leaves of tree t.

    >>> t = Tree(3, [Tree(4), Tree(5, [Tree(6), Tree(7)])])
    >>> largest_leaf(t)
    7
    """
    if is_leaf(t):
        return t.label
    return max([largest_leaf(b) for b in t.branches])


def has_path[T](t: Tree[T], p: list[T]) -> bool:
    """Return whether tree t has a path from the root with labels p
    >>> u = Tree(5, [Tree(6), Tree(7)])
    >>> t = Tree(3, [Tree(4), u])
    >>> has_path(t, [5, 6]) # This path is not from the root of t
    False
    >>> has_path(u, [5, 6])        # This path is from the root of u
    True
    >>> has_path(t, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if p == ____:  # when len(p) is 1
        return True
    elif t.label != ____:
        return False
    else:
        "*** YOUR CODE HERE ***"
