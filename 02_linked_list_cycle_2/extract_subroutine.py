from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        meeting_node = detectMeetingNode(head)
        if meeting_node is None:
            return None

        leading_node = meeting_node
        following_node = head
        while leading_node is not following_node:
            leading_node = leading_node.next
            following_node = following_node.next

        return leading_node


def detectMeetingNode(head: Optional[ListNode]) -> Optional[ListNode]:
    """Detect meeting node when using Floyd's cycle-finding algorithm."""
    faster_node = head
    slower_node = head

    while faster_node is not None and faster_node.next is not None:
        faster_node = faster_node.next.next
        slower_node = slower_node.next

        if faster_node is slower_node:
            return faster_node

    return None