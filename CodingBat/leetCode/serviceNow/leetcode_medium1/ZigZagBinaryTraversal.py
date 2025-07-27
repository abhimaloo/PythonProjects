from collections import deque
from typing import List, Optional
"""
Given a binary tree, return the zigzag level order traversal of its nodes’ values. 
(i.e., from left to right, then right to left for the next level and alternate between).

"""
# TreeNode class definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse the level if direction is right to left
            if not left_to_right:
                level_nodes.reverse()

            result.append(level_nodes)
            left_to_right = not left_to_right  # Toggle direction for next level

        return result


"""
Use a queue for normal level order traversal (BFS).
Keep a flag to indicate direction of traversal for each level.
Reverse the level list when the flag says right-to-left.

Explanation:
Check if root is None: return empty list if yes.
Use a queue to perform BFS level-order traversal.
For each level:
Extract all nodes.
Collect their values in a list.
Append children to the queue for next level.
If zigzag direction is right-to-left, reverse the list of values for that level.
Toggle direction for the next level.
Time Complexity:
O(n) — Each node is visited exactly once.
Space Complexity:
O(n) — In worst case, queue stores all nodes at the last level.

"""