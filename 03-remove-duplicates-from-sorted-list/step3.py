# Step3の感想
# 頭の中でbeginとendがシャクトリムシのようにリストを走査していくところを想像しながら書いた。
# 3回連続で3分以内に書き切れたので一区切りとする。

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # When the list is empty.
        if head is None:
            return None

        deduplicated_list_head = ListNode(head.val, None)
        deduplicated_list_tail = deduplicated_list_head

        begin = head
        end = head
        while begin is not None:
            while end is not None and begin.val == end.val:
                end = end.next

            deduplicated_list_tail.next = ListNode(end.val, None) if end is not None else None
            deduplicated_list_tail = deduplicated_list_tail.next
            begin = end

        return deduplicated_list_head
