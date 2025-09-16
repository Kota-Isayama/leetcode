# Step1での感想
# 読みやすいコードを書きにくい！同じ値が続いているところを右半開区間で表現しようとしているが、伝わるだろうか。
# ちなみに右半開区間を表す時（というかC++のiteratorとかだったと思うが、最初を含んで最後を含まないようなポインタを扱う時）はbeginとendを使うのが標準らしい。Readable code.
# 受け取ったリストに変更を与えるコードにしちゃったのでstep2では副作用を消したい（答え合わせでidを使って比較していなければ）。

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

        deduplicated_list_head = head
        deduplicated_list_tail = head

        # 同じ値をもつノードの区間を求める。ただし右半開区間であり、endは同値性が初めて崩れるnode。と言うつもりで以下のコードを書いている。
        begin = head
        end = head
        while begin is not None:
            while end is not None and begin.val == end.val:
                end = end.next

            deduplicated_list_tail.next = end
            deduplicated_list_tail = end
            begin = end

        return deduplicated_list_head