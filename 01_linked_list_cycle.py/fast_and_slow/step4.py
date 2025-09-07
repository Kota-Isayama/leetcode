class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head : ListNode | None) -> bool:
        """Implements Hare and Tortoise algorithm."""
        faster = head
        slower = head

        while faster is not None and faster.next is not None:
            faster = faster.next.next
            slower = slower.next

            if faster is slower:
                return True

        return False
