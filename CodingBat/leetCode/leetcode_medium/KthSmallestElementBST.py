# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        #Inorder Traversal Loop continues while there are nodes left to visit
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left   # Keep going left and pushing nodes on the stack (like recursive calls)

            cur = stack.pop()   #Process the leftmost node
            n += 1              #Increment count — this is the n-th node in sorted order

            if n == k:           #If this is the kth smallest, return its value immediately
                return cur.val
            cur = cur.right        #After processing a node, move to its right child

"""
Given a Binary Search Tree (BST) and an integer k, return the kth smallest element in the BST.
In a BST:
Inorder traversal (Left → Root → Right) gives the sorted order of the values.
So, the kth node visited during inorder traversal is the kth smallest element.
stack: to simulate recursion (iterative inorder traversal)
n: counter to track how many nodes we've visited
cur: pointer to the current node

Time: O(H + k)
H = height of tree (worst case O(n) for skewed trees, O(log n) for balanced)
Space: O(H) for the stack

"""