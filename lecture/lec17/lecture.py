from lab.lab05.tree import Tree


def big(t: Tree[int]) -> int:
    """
    Take a Tree instance containing integer label.
    Return number of node in t whose labels are larger than all labels of their ancestor node.
    Assume the root label is always larger than all its ancestor, since it has no ancestor.
    """

    return 0


def count_big(t: Tree, n: int) -> int:
    """Return the number of paths in t that have a sum >= to n"""
    return 0


def print_big(t: Tree, n: int):
    """Print the paths in t that have a sum >- to n"""


def only_paths(t: Tree[int], n: int) -> Tree[int] | None:
    """
    Takes a Tree of integers t and an int n.
    It returns a Tree with only the nodes of t that are on a path from the root to a leaf with labels that sum to n. or None if no path sums to n.
    """
    return None
