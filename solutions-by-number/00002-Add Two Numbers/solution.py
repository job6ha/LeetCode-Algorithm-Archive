# Definition for singly-linked list.
import string
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _get_value(self, node: Optional[ListNode]) -> int:
        number = ""
        while node.next is not None:
            number += str(node.val)
            node = node.next
        number += str(node.val)

        return int(number[::-1])
    
    def _make_node(self, value: int) -> Optional[ListNode]:
        value_str = str(value)
        head = None
        for val in value_str:
            node = ListNode(int(val))
            node.next = head
            head = node
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_value = self._get_value(l1)
        l2_value = self._get_value(l2)

        calculated_value = l1_value + l2_value

        return self._make_node(calculated_value)

def stringify_node(node: Optional[ListNode]):
    string = ""
    while node is not None:
        string += str(node.val)
        node = node.next
    return string

def test_solution():
    print("=== Case 1 ===")
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    expected = ListNode(7, ListNode(0, ListNode(8)))

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    assert result == expected, f"Expected {stringify_node(expected)} but got {stringify_node(result)}"

    print("=== Case 2 ===")
    l1 = ListNode(0)
    l2 = ListNode(0)
    expected = ListNode(0)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    assert result == expected, f"Expected {stringify_node(expected)} but got {stringify_node(result)}"

    print("=== Case 3 ===")

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    expected = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    assert result == expected, f"Expected {stringify_node(expected)} but got {stringify_node(result)}"

    print("All cases passed")

if __name__ == "__main__":
    print("Starting tests...")
    test_solution()
    print("All tests passed")