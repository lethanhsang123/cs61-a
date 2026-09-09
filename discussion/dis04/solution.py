def paths(m: int, n: int) -> int:
    """
    Return the number of paths from one corner of an M by N grid
    to the opposite corner.

    Concept: Track the insect's current position from one corner
    to the opposite corner.

    Base cases:
    - Outside the grid → 0 paths
    - Reach the opposite corner → 1 path
    """

    def path_from(x, y):
        if x >= m or y >= n:
            return 0
        elif x == m - 1 and y == n - 1:
            return 1
        else:
            return path_from(x, y + 1) + path_from(x + 1, y)

    return path_from(0, 0)

def paths2(m, n):
    """
    Concept: Track the size of the remaining grid.

    Base case:
    If there is only one row or one column remaining,
    there is exactly one possible path.
    """

    if m == 1 or n == 1:
        return 1

    return paths2(m - 1, n) + paths2(m, n - 1)

def max_product(s):
    """Return the maximun product of non-consecutive elements of s"""
    l = len(s)
    max = s[0];
    
    return max