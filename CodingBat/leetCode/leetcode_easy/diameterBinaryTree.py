
"""Time Complexity: O(n) — each node is visited once.

Space Complexity: O(h) — where h is the height of the tree (due to recursion stack)."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        largest_diameter = [0]

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height
            largest_diameter[0] = max(largest_diameter[0], diameter)
            return 1 + max(left_height, right_height)

        height(root)
        return largest_diameter[0]


# execution

# Build tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

# Create instance and call method
sol = Solution()
print(sol.diameterOfBinaryTree(root1.left))  # Output: 3









