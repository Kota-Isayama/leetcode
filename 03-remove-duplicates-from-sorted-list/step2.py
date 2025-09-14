# Step2の感想
# 受け取ったリストに対する副作用がないように実装を行なった。
# その結果として、deduplicated_list_tailの更新に場合わけが生じてしまった。
# 「途中まで出来上がっているリスト」の末尾に新たにノードをくっつける考え方の時点で、最初に先頭ノードを用意しておく必要があるので、以下のコードの構造から抜け出せない気がする。


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        # 新しく作成していくリストの先頭ノードと、出来上がっているところまでの末尾ノード
        deduplicated_list_head = ListNode(head.val, None)
        deduplicated_list_tail = deduplicated_list_head

        # 同じ値をもつノードの区間を求める。ただし右半開区間。
        begin = head
        end = head
        while begin is not None:
            # I will have begin.val == begin.next.val == begin.next.next.val == ... == end.prev.val != end.val
            while end is not None and begin.val == end.val:
                end = end.next

            # 末尾ノードの伸長
            deduplicated_list_tail.next = ListNode(end.val, None) if end is not None else None
            deduplicated_list_tail = deduplicated_list_tail.next
            begin = end

        return deduplicated_list_head
