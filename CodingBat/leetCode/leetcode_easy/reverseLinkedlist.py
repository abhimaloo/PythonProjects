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
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


# example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

solution = Solution()
reversed_head = solution.reverseLinkedList(head)

# reverse the linked list
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next
