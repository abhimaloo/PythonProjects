"""
Time Complexity: O(n)
 Space Complexity: O(1)

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow




# Helper: Convert list to linked list
def list_to_linkedlist(values):
    dummy = ListNode()
    head = dummy
    for val in values:
        head.next = ListNode(val)
        head = head.next
    return dummy.next

# Helper: Print linked list from a given node
def print_linkedlist(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

# 🧪 Test Cases
def run_tests():
    sol = Solution()
    values = [10, 20, 30, 40]
    test1 = list_to_linkedlist(values)
    print("Test 1 Output:")
    print_linkedlist(sol.middleNode(test1))  # Expected: 3 -> 4 -> 5



run_tests()
