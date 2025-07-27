class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete the ListNode
        left.next = left.next.next
        return dummy.next


"""
A dummy node is created that points to the head.

This handles edge cases like when the head itself needs to be removed.

Two pointers:

right will move ahead by n steps.

left will eventually point to the node before the one to remove.

Now the right pointer is n nodes ahead of left.

So when right reaches the end, left will be just before the node to delete.

When right is None, left is just before the node to delete.

Skip over the n-th node from the end.

Return the actual head of the list (since dummy was a placeholder).

"""