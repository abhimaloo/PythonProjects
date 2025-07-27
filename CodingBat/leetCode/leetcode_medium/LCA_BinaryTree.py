# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None   # If the node is None, return None.
        if root == p or root == q:     #If the current node is either p or q, return it.
            return root

        #Recursively search in the left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right


"""

Time	O(n) — visit each node once
Space	O(h) — call stack (height of tree)


If both left and right calls return non-None, it means:

One node was found in the left subtree.

The other was found in the right subtree.

So the current node is the LCA.

If only one side returned a node (p or q or their LCA), return it.

If both are None, it returns None.


"""
