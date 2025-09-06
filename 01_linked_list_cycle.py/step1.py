import dataclasses
from typing import Optional


@dataclasses.dataclass
class ListNode:
    val: int
    next: Optional["ListNode"]


class Solution:
    def hasCycle(self, head : ListNode | None) -> bool:
        if head is None:
            return False

        visited_indices: set[ListNode] = set()
        current_node = head
        while current_node.next is not None:
            if current_node.next in visited_indices:
                return True

            visited_indices.add(current_node.next)
            current_node = current_node.next

        return False
