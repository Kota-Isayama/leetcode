# Step1の感想
# 83. Remove Duplicates from Sorted Listとほぼ同じ感覚で書いた。
# beginとendで同じ値を持つ部分リストの半開区間のようなものを舐めていく。
# ただし、83. Remove Duplicates from Sorted Listと違ったのは、headが答えのリストの先頭に入るかどうか不明であるため
# 先頭を作成するコードが後ろの方に入ってしまい、ちょっと気持ち悪い。


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        deduplicated_list_head = None
        deduplicated_list_tail = None

        begin = head
        end = head
        while begin is not None:
            # I will check the `begin` has duplicated number in the given list.
            while end is not None and begin.val == end.val:
                end = end.next

            # the `begin` has a unique value in the list.
            if begin.next is end:
                # The `begin` is the first node of the deduplicated list.
                if deduplicated_list_head is None:
                    deduplicated_list_head = ListNode(begin.val, None)
                    deduplicated_list_tail = deduplicated_list_head
                else:
                    deduplicated_list_tail.next = ListNode(begin.val, None)
                    deduplicated_list_tail = deduplicated_list_tail.next

            begin = end

        return deduplicated_list_head
