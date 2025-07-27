class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        #  # Step 1: Find the middle using slow and fast pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #  # Step 2: Reverse second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Compare first half and reversed second half
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

"""
Given the head of a singly linked list, determine whether it's a palindrome.
A palindrome is a sequence that reads the same forward and backward.
✅ Optimal Solution (O(n) time, O(1) space)
We'll use two pointers (slow and fast) to find the middle, reverse the second half, and compare the two halves.

Step-by-Step Explanation
Suppose the input is:

1 → 2 → 2 → 1
🔹 Step 1: Find the middle
Use two pointers:

slow moves 1 step

fast moves 2 steps

At the end of the loop:

slow is at the middle node

🔹 Step 2: Reverse the second half
From:

2 → 1
To:

1 → 2
🔹 Step 3: Compare both halves
First half: 1 → 2
Reversed second half: 1 → 2
Compare node by node.

✅ All values match → It's a palindrome.


"""