# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        visited_nodes = {head}
        last_checked_node = head
        while (next_node := last_checked_node.next) is not None:
            if next_node in visited_nodes:
                return True

            visited_nodes.add(next_node)
            last_checked_node = next_node

        return False
