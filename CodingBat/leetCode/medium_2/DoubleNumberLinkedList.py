class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleNumber(self, head: ListNode) -> ListNode:
        def reverse(node):
            prev = None
            current = node

            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            return prev

        head = reverse(head)

        carry = 0
        current = head

        while current:
            total = current.val * 2 + carry
            current.val = total % 10
            carry = total // 10
            if current.next is None and carry > 0:
                current.next = ListNode(0)  # Extend list if carry left
            current = current.next

        head = reverse(head)
        return head

"""
Approach:
Since the list is in forward order, we can do either:
Reverse the list, double it like in normal addition with carry, then reverse it back.
Or, recursive approach to process from left to right with carry passing backward.
✅ Step-by-step (Reverse approach):
Reverse the linked list.
Double each digit with carry.
Reverse back the result.
"""