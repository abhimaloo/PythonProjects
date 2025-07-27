# time complexity = o(h)

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.value > cur.value and q.value > cur.value:
                cur = cur.right
            elif p.value < cur.value and q.value < cur.value:
                cur = cur.left
            return cur


"""Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6."""

#example usage
# Example Usage:
# Construct a sample binary tree
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# Nodes for which to find the LCA
p = root.left  # Node with value 2
q = root.right  # Node with value 8

# Create an instance of the Solution class
solution = Solution()

# Call the lowestCommonAncestor method
lca = solution.lowestCommonAncestor(root, p, q)

# Print the value of the LCA node
print(lca.value)




