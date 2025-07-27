# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head) :
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        # If it's the start of duplicates
        while cur and cur.next:
            if cur.value == cur.next.value:
                dup_value = cur.value
                # Skip all nodes with this value
                while cur and cur.value == dup_value:
                    cur = cur.next
                prev.next = cur
            else:
                prev = prev.next  # Move prev only if no deletion
                cur = cur.next
        return dummy.next








