# Step4
# いただいた指摘
# - inplaceで処理をするなら、deduplicated_list_headやdeduplicated_list_tailといった変数を用意するのは冗長に思う
#   - 確かにあえて変数を置き直すとinplace感が薄れていると感じる。inplaceでは変数を無闇に置き直すことはやめてみる。
# - endが動いていくことに関しては特に違和感を覚えない。たとえばtotal_sum = 0としてtotal_sum += some_numberみたいな書き方は普通にするし
#   最終的にどのような値になるのかが事前にわかることは読みやすさに繋がる。
#   - 確かにtotal_sumなんてよくやる書き方で本質的にそことの差はないので、今後はあまり気にしすぎないようにする。


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesInPlace(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head  # 無駄に変数を定義しすぎない

        while node is not None:
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next
            node = node.next

        return head

    def deleteDuplicatesOutOfPlace(self, head: Optional[ListNode]) -> Optional[ListNode]:
        deduplicated_list_head = ListNode(head.val)
        deduplicated_list_tail = deduplicated_list_head

        begin = head
        while begin is not None:
            end = self.__get_next_distinct_value_node(begin)  # より関数の事実に即した名前
            if end is not None:
                deduplicated_list_tail.next = ListNode(end.val)
                deduplicated_list_tail = deduplicated_list_tail.next

            begin = end

        return deduplicated_list_head

    def __get_next_distinct_value_node(self, node: Optional[ListNode]) -> Optional[ListNode]:
        while node.next is not None and node.val == node.next.val:
            node = node.next

        return node.next
