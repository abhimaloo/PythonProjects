# Definition for a binary tree node.
"""
 Time Complexity: O(n)
Each node is visited once → n is the number of nodes.

📦 Space Complexity:
Worst-case (skewed tree): O(n) recursion stack.

Best-case (balanced tree): O(log n) recursion stack height.
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root) :
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

#Execution

"""Input: root = [3,9,20,null,null,15,7]
Output: 3
"""

solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(solution.maxDepth(root))


"""Iterative Version using BFS (Level-order Traversal):
python
Copy
Edit
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth"""



