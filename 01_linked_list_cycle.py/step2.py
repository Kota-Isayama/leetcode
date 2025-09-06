import dataclasses
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head : ListNode | None) -> bool:
        if head is None:
            return False

        visited_nodes: set[ListNode] = set()
        current_node = head
        while (next_node := current_node.next) is not None:
            if next_node in visited_nodes:
                return True

            visited_nodes.add(next_node)
            current_node = next_node

        return False
