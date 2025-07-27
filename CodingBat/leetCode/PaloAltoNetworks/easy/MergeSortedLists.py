# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# time cmplexity o (n)

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2

        return dummy.next

"""
dummy is a placeholder to start building the result list.
cur is a pointer that moves along the new merged list.
Compare the heads of both lists.
Link cur.next to the smaller node.
Move that list's pointer forward.
Move cur forward.

Attach the Remaining Nodes:
At this point, one list is None.

The other list might still have nodes — just attach the remainder.
return dummy.next
dummy was just a starting point.
dummy.next is the real head of the merged sorted list.



"""