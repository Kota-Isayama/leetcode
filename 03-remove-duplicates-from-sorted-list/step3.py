# Step3の感想
# 頭の中でrun_begin_nodeとnodeがシャクトリムシのようにリストを走査していくところを想像しながら書いた。
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

        run_begin_node = head
        while run_begin_node is not None:
            node = run_begin_node
            while node is not None and run_begin_node.val == node.val:
                node = node.next

            deduplicated_list_tail.next = ListNode(node.val) if node is not None else None
            deduplicated_list_tail = deduplicated_list_tail.next
            run_begin_node = node

        return deduplicated_list_head

    def deleteDuplicatesWithSideEffect1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # When the list is empty.
        if head is None:
            return None

        node = head
        while node is not None:
            if node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head

    def deleteDuplicatesWithSideEffect2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # When the list is empty.
        if head is None:
            return None

        node = head
        while node is not None:
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next

            node = node.next

        return head
