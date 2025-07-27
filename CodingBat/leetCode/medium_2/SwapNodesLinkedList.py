class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # Step 1: Determine the length
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Find k-th node from beginning and end
        first = head
        for _ in range(k - 1):
            first = first.next

        second = head
        for _ in range(length - k):
            second = second.next

        # Step 3: Swap values
        first.val, second.val = second.val, first.val

        return head
