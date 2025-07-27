class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = headA
        l2 = headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

"""

How It Works:
Two pointers, l1 and l2, are initialized to the heads of the two lists.

Both pointers traverse their respective lists.

When either pointer reaches the end (None), it is redirected to the head of the other list.

Eventually, if the lists intersect, the two pointers will meet at the intersection node after at most lengthA + lengthB steps.

If they do not intersect, both pointers will eventually become None (end of both lists), and the loop will terminate.
Time: O(m + n), where m and n are the lengths of the two lists.

Space: O(1) — constant extra space.

"""