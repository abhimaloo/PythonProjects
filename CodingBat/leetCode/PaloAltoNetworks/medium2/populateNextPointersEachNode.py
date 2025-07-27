"""
Given a perfect binary tree (all leaves are on the same level, and every parent has two children),
populate each node's next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to None.
"""
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root

        while leftmost.left:
            current = leftmost

            while current:
                # Connect left child to right child
                current.left.next = current.right

                # Connect right child to next node's left child if exists
                if current.next:
                    current.right.next = current.next.left

                current = current.next

            leftmost = leftmost.left

        return root
"""
Approach:
Use the already established next pointers to traverse nodes at the current level to set the next pointers for the next level.
Start from the root, go level by level.
For each node at a level:
Connect its left child's next pointer to its right child.
Connect its right child's next pointer to the next node’s left child (if next exists).

Explanation:
Initialize leftmost as the root — this will track the leftmost node of each level.
While there is a next level (leftmost.left exists):
Traverse the current level using current pointer.
Connect:
current.left.next = current.right
current.right.next = current.next.left (if current.next exists)
Move current to current.next to connect nodes horizontally.
Move down to the next level (leftmost = leftmost.left).

Time and Space Complexity:
Time Complexity: O(n) — each node is visited once.
Space Complexity: O(1) — only pointers used, no extra data structures.

"""