"""
Given a binary tree where each node contains a digit (0-9),
each root-to-leaf path represents a number formed by concatenating the digits along the path.
Return the total sum of all root-to-leaf numbers.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_number):
            if not node:
                return 0   #If the node is None, return 0. This is the base case to prevent null pointer errors during recursion

            current_number = current_number * 10 + node.val   #Builds the number as we go deeper in the tree.

            # If leaf node, return the current number
            if not node.left and not node.right:
                return current_number

            # Otherwise, sum left and right subtree
            return dfs(node.left, current_number) + dfs(node.right, current_number)

        return dfs(root, 0)   #Start DFS from the root, with an initial number of 0.

"""
Approach:
Use DFS (Depth First Search) to traverse the tree.
Keep track of the current number formed by the path so far.
When reaching a leaf, add the current number to the sum.
Explanation:
Start from root with current number 0.
At each node, multiply current number by 10 and add node’s value.
When a leaf is reached, return the formed number.
Sum the values returned from left and right children recursively.
Time and Space Complexity:
Time: O(n), n = number of nodes, each visited once.
Space: O(h), h = height of the tree (recursive call stack).

This is a clean, recursive DFS implementation that efficiently computes the sum of all root-to-leaf numbers in a binary tree. 
It's optimal in both readability and performance.





"""