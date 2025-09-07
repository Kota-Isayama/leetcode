class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head : ListNode | None) -> bool:
        # Corner case
        if head is None or head.next is None:
            return False

        faster = head
        slower = head

        # Loop until the faster node catch up with slower or faster reaches the tail.
        while faster is not None and faster.next is not None:  # If the condition is not satisfied, faster reaches the tail. The condition written at step1 was not correct... `or` should not be used but `and` should...
            faster = faster.next.next
            slower = slower.next

            if faster == slower:  # faster reaches slower.
                return True

        return False
