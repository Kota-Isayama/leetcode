# Step2の感想
# 受け取ったリストに対する副作用がないように実装を行なった。
# その結果として、deduplicated_list_tailの更新に場合わけが生じてしまったが、特に処理が長いとかではないので自然な流れだと思いそのまま。
#
# PRレビュー依頼を出した後ではあるのだが...
# 過去の他の方のPRを読んでみて、受け取ったリストに対して変更を加える実装２つも行ってみた。
# 1つ目の方はループが一つだけのものであるが、条件分岐した先の更新処理の性質が全然違うため、個人的にはあまり好きではない。
# 一つのループの中で動くものが違うから。nodeとnode.next。
# 2つ目の方はループが二つ現れるが、値が同じである限りnextから外して、nodeを次の値を持つものに更新する、と言う自然な言語化ができて好き。
# この場合は、それぞれのループの中で動くものが必ず同じであるから。


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
        run_begin_node = head
        while run_begin_node is not None:
            node = run_begin_node
            # I will have run_begin_node.val == run_begin_node.next.val == run_begin_node.next.next.val == ... == node.prev.val != node.val
            while node is not None and run_begin_node.val == node.val:
                node = node.next

            # 末尾ノードの伸長
            deduplicated_list_tail.next = ListNode(node.val, None) if node is not None else None
            deduplicated_list_tail = deduplicated_list_tail.next
            run_begin_node = node

        return deduplicated_list_head

    def deleteDuplicatesWithSideEffect1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        node = head
        while node.next is not None:
            if node.val == node.next.val:  # この場合の更新処理と
                node.next = node.next.next
            else:  # この場合の更新処理の性質が全然違うので、ちょっと気持ち悪い。
                node = node.next

        return head

    def deleteDuplicatesWithSideEffect2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        node = head
        while node is not None:  # こちらの方がnodeが毎回後ろに移動していて、直感に合うループ処理に思える。
            # Change node.next until node.next has different value or node.next become None.
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next

            node = node.next

        return head