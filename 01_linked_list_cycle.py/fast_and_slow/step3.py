class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head : ListNode | None) -> bool:
        # Corner case
        if head is None or head.next is None:
            return False

        # 2 variables that traverses a list
        faster = head
        slower = head

        while faster is not None and faster.next is not None:
            faster = faster.next.next
            slower = slower.next

            if faster == slower:
                return True

        return False
