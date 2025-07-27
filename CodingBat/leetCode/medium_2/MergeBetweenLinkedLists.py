class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        current = dummy

        # Step 1: Find node at position a - 1
        for _ in range(a):
            current = current.next
        prevA = current

        # Step 2: Find node at position b
        for _ in range(b - a + 1):
            current = current.next
        afterB = current.next

        # Step 3: Connect prevA -> list2
        prevA.next = list2

        # Step 4: Connect end of list2 to afterB
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        tail2.next = afterB

        return dummy.next


"""
Plan:
Traverse list1 to find:
prevA: the node at index a-1
afterB: the node at index b+1

Connect:
prevA.next = head of list2
Last node of list2 → connect to afterB

"""