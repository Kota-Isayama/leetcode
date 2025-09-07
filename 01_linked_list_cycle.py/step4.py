from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checked_nodes = set()
        node = head
        
        while node is not None:
            if node in checked_nodes:
                return True
            checked_nodes.add(node)
            node = node.next

        return False
