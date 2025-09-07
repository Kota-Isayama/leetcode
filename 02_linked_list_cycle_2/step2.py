from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        faster = head
        slower = head

        while faster is not None and faster.next is not None:
            faster = faster.next.next
            slower = slower.next

            if faster is slower:
                break

        # When there is no cycle.
        if faster is None or faster.next is None:
            return None

        predecessor = faster
        successor = head

        while predecessor is not successor:
            predecessor = predecessor.next
            successor = successor.next

        return predecessor
