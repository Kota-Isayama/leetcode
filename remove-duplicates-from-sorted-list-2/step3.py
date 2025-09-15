# Step3
# Step2の3つ目の実装方針で副作用なし版とあり版を両方書いた。
# deduplicated_list_tailに繋いでいくListNodeがオリジナルのリストのものかどうかしか差はない。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, Literal


class Solution:
    __DUMMY_HEAD_VALUE = -101

    def deleteDuplicatesWithNoSideEffect(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(self.__DUMMY_HEAD_VALUE)
        deduplicated_list_tail = dummy_head

        begin = head
        while begin is not None:
            end = self.__get_same_value_interval_end(begin)
            if begin.next is end:
                deduplicated_list_tail.next = ListNode(begin.val)  # インスタンス化しなおしたノードを繋げる。
                deduplicated_list_tail = deduplicated_list_tail.next

            begin = end

        return dummy_head.next

    def deleteDuplicatesWithSideEffect(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(self.__DUMMY_HEAD_VALUE)
        deduplicated_list_tail = dummy_head

        begin = head
        while begin is not None:
            end = self.__get_same_value_interval_end(begin)
            if begin.next is end:
                deduplicated_list_tail.next = begin  # オリジナルのリストのノードを繋げる。
                deduplicated_list_tail = deduplicated_list_tail.next

            begin = end

        return dummy_head.next

    def __get_same_value_interval_end(self, begin: ListNode) -> Optional[ListNode]:
        """A helper function."""
        node = begin
        while node.next is not None and node.val == node.next.val:
            node = node.next
        return node.next
