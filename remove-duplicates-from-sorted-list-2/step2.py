# Step2の感想
# 3つの実装を行なってみた
#
# 1つ目
# 基本的にstep1と同じだが、最初のガード節を外した。
# 先頭へのノードの追加が後ろの方に出てくるのは相変わらずであるため、他の方のPRを参考にしつつ、より良い書き方を考え始める。
#
# 2つ目
# いくつかのPRでも書かれていた方法で、ダミーのheadを作成することによってコードを簡潔にする実装で書いた。
# ダミーであることを明示するために、イニシャライザに与える値は制約から外れる-101としたが、これは実装の詳細であり外部に漏らすべき情報ではないため、
# private属性で定数を定義した。
# 今回の問題で主にフォーカスが当たっているであろう、同じ値が続く区間の削除よりも、ユニークな値を持つリストの抽出の処理が目立ってしまっており、
# 分かりにくさを感じる。
#
# 3つ目
# よく考えてみると、処理を以下のように言語化できる。
# beginはbegin.valと同じ値を持つ区間の先頭であるという不変条件のもと..
# 1. begin.valと同じvalをもつノードが繋がった区間のend（beginから辿って初めてbegin.val != end.valとなるノード）を探す
#   a. endがbeginの次ならbeginはuniqueなvalを持つのでそれをtailに付け加える
#   b. endがbeginの次より後ノードならbeginのvalはuniqueではなかったのでtailには付け加えない
# 2. beginをendで更新してbeginがNoneになるまで（本当に末尾に至るまで）繰り返す。
# このうち、1つ目の処理を関数として切り出すとコードが上記の自然言語を自然に翻訳したものになっている。
#
# 個人的に3つ目がお気に入り。答えのリストに含めるときと含めないときとで自然に処理を共通化できている。関数化による処理の抽象化の威力も実感中。


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Pure functional method."""
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
                if deduplicated_list_head is None:  # ここで初めて答えのリストの先頭がセットされる。関数の中で後半の方に出てきてしまっており、直感的でない。
                    deduplicated_list_head = ListNode(begin.val, None)
                    deduplicated_list_tail = deduplicated_list_head
                else:
                    deduplicated_list_tail.next = ListNode(begin.val, None)
                    deduplicated_list_tail = deduplicated_list_tail.next

            begin = end

        return deduplicated_list_head


    __DUMMY_UNIQUE_VALUE = -101

    def deleteDuplicatesWithDummy1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Side effective method."""
        dummy_head = ListNode(self.__DUMMY_UNIQUE_VALUE)
        deduplicated_list_tail = dummy_head
        node = head

        while node is not None:
            # the `node` has a unique value.
            if node.next is None or node.val != node.next.val:
                deduplicated_list_tail.next = node
                deduplicated_list_tail = deduplicated_list_tail.next
                node = node.next
                continue

            # the `node` doesn't have a unique value.
            while node.next is not None and node.val == node.next.val:
                node.next = node.next.next

            node = node.next

        return dummy_head.next

    def deleteDuplicatesWithDummy2(self,  head: Optional[ListNode]) -> Optional[ListNode]:
        """Side effective method."""
        dummy_head = ListNode(self.__DUMMY_UNIQUE_VALUE)
        deduplicated_list_tail = dummy_head
        begin = head

        while begin is not None:
            end = self.__get_same_value_interval_end(begin)
            # When there are no nodes with same value.
            if begin.next is end:
                deduplicated_list_tail.next = begin
                deduplicated_list_tail = deduplicated_list_tail.next

            begin = end

        return dummy_head.next


    def __get_same_value_interval_end(self, begin: ListNode) -> Optional[ListNode]:
        """A helper function to get the end node which has the same value."""
        node = begin
        while node.next is not None and node.val == node.next.val:
            node = node.next
        return node.next
