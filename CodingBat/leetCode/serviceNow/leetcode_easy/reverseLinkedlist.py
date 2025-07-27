# Time Complexity: O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseLinkedList(self, head):
        cur = head
        prev = None

        while cur:
            temp = cur.next  # store the next node temporarily so we dont loose track of the rest of the list
            cur.next = prev  # reverse the link now ( flipping direction )
            prev = cur       # move prev one step forward and cur is now the last processed node
            cur = temp       # move cut to the next node in the original list ( which we saved in temp)

        return prev           # when cur becomes None , loop emds and prev pointing to new head of the reversed list

# example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
solution = Solution()
reversed_head = solution.reverseLinkedList(head)
#reverse the linked list
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next

