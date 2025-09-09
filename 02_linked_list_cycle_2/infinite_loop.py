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

        while True:
            if faster is None or faster.next is None:
                return None

            faster = faster.next.next
            slower = slower.next

            if faster is slower:
                break

        predecessor = faster
        successor = head

        while predecessor is not successor:
            predecessor = predecessor.next
            successor = successor.next

        return predecessor
