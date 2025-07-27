# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #This is the base case: if both lists are empty, return None. This means there is no tree to build.
        if not preorder and not inorder:
            return None
        #The first element of preorder is always the root of the current (sub)tree.
        root = TreeNode(preorder[0])
        #Finds the index of the root node in the inorder list. This splits the inorder list into:
        mid = inorder.index(preorder[0])

        #Skip the root (preorder[0]) and recursively build the left subtree.
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # Everything after the left subtree in preorder goes to the right subtree.
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

"""
Background
Preorder traversal: Root -> Left -> Right
Inorder traversal: Left -> Root -> Right
Given these two sequences, you can uniquely reconstruct the original binary tree.

Finds the index of the root node in the inorder list. This splits the inorder list into:

inorder[:mid] → the left subtree

inorder[mid+1:] → the right subtree


time cpmplexcity

Current version: O(n^2) due to repeated list slicing and index() calls.
space 
Due to recursion stack and list slicing → also O(n^2)


=


"""