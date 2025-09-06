from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge case
        if head is None or head.next is None:
            return False

        visited_nodes : set[ListNode] = set()
        visited_nodes.add(head)
        current_node = head

        while (next_node := current_node) is not None:
            if next_node in visited_nodes:
                return True

            visited_nodes.add(next_node)
            current_node = next_node

        return False
