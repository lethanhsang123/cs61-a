from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Tree[T]:
    label: T
    branches: list[Tree[T]] = field(default_factory=list)  # branches defaults to []


def is_leaf(t: Tree) -> bool:
    "Return whether a Tree is a leaf with no branches."
    return not t.branches
