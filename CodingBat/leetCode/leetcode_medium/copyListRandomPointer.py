class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Clone each node and insert it next to original
        curr = head
        while curr:
            copy = Node(curr.val, curr.next, None)
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers to the copy nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the two lists
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next

        return copy_head



"""
 Time and Space Complexity:
Time: O(n)

Space: O(1) (since we don’t use extra hash maps)

"""