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
    if not p:
        return False
    if len(p) == 1 and p[0] == t.label:  # when len(p) is 1
        return True
    elif len(p) == 1 and t.label != p[0]:
        return False
    else:
        return (t.label == p[0]) and any(
            has_path(branch, p[1:]) for branch in t.branches
        )


def find_path[T](t: Tree[T], x: T) -> list[T] | None:
    """Return a list of the labels along a path from the root of t to a node
    labeled x, or None if no node is labeled x.

    >>> u = Tree(5, [Tree(6), Tree(7)])
    >>> t = Tree(3, [Tree(4), u])
    >>> find_path(t, 5)
    [3, 5]
    >>> find_path(t, 4)
    [3, 4]
    >>> find_path(t, 6)
    [3, 5, 6]
    >>> find_path(u, 6)
    [5, 6]
    >>> pint(find_path(t, 2))
    None
    """
    if t.label == x:
        return [t.label]
    for branch in t.branches:
        path = find_path(branch, x)
        if path is not None:
            return [t.label] + path
    return None


def find_path[T](t: Tree[T], x: T) -> list[T] | None:
    """Return a list of the labels along a path from the root of t to a node
    labeled x, or None if no node is labeled x.

    >>> u = Tree(5, [Tree(6), Tree(7)])
    >>> t = Tree(3, [Tree(4), u])
    >>> find_path(t, 5)
    [3, 5]
    >>> find_path(t, 4)
    [3, 4]
    >>> find_path(t, 6)
    [3, 5, 6]
    >>> find_path(u, 6)
    [5, 6]
    >>> pint(find_path(t, 2))
    None
    """
    if t.label == x:
        return [t.label]
    for branch in t.branches:
        path = find_path(branch, x)
        if path is not None:
            return [t.label] + path
    return None


def only_paths(t: Tree[int], n: int) -> Tree[int] | None:
    """Return a tree with only the nodes of t along paths from the root to a leaf of t
    for which the node labels of the path sum to n. If no paths sum to n, return None.

    >>> print(only_paths(Tree(5, [Tree(2), Tree(1, [Tree(2)]), Tree(1, [Tree(1)])]), 7))
    5
      2
      1
        1
    >>> t = Tree(3, [Tree(4), Tree(1, [Tree(3, [Tree(2)]), Tree(2, [Tree(1)]), Tree(5), Tree(3)])])
    >>> print(only_paths(t, 7))
    3
      4
      1
        2
          1
        3
    >>> print(only_paths(t, 9))
    3
      1
        3
          2
        5
    >>> print(only_paths(t, 3))
    None
    """
    if ____:
        return t
    new_branches = [____ for b in t.branches]
    if ____(new_branches):
        return Tree(t.label, [b for b in new_branches if ____])
