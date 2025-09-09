from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        faster_node = head
        slower_node = head

        while True:
            if faster_node is None or faster_node.next is None:
                return None
            faster_node = faster_node.next.next
            slower_node = slower_node.next
            if faster_node is slower_node:
                break

        leading_node = faster_node
        following_node = head
        while leading_node is not following_node:
            leading_node = leading_node.next
            following_node = following_node.next

        return leading_node
