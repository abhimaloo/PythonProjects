# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True  # An empty subtree is always valid. base case
            if not (node.val > left and node.val < right):
                return False   #Value Violation Check:

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right)) #  Recursive Check:

        return valid(root, float('-inf'), float('inf'))

solution = Solution()

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(solution.isValidBST(root))
"""
This function checks whether a binary tree is a valid Binary Search Tree (BST) 
using a recursive DFS with value range constraints.
last step 
Recursively validate:
Left child: must be between left and node.val
Right child: must be between node.val and right
Starts with the widest possible range, and narrows down as recursion descends.
Complexity	Value
Time	O(n) — visit each node once
Space	O(h) — call stack (h = height of tree), worst-case O(n) in unbalanced tree








"""

