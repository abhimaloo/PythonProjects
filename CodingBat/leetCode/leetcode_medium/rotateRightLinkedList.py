# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
#If the list is empty, just return it.


#Traverse the list to find the length and the tail node.
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

#Normalize k

        k = k % length
        if k == 0:
            return head


#Find new head (after rotation)
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead



"""
If k >= length, rotating more than once is the same as rotating k % length times.

If k == 0 (after modulo), the list stays the same.

Move cur to the (length - k - 1)th node.

This node will become the new tail after rotation.

cur.next is the new head of the rotated list.

Break the list at cur → cur.next = None

Connect the original tail to the original head → tail.next = head

Return newHead
"""