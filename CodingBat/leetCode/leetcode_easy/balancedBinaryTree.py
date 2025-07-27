# Definition for a binary tree node.
# time complexity = o(n)
#space = o(h)
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0

            left_height = height(root.left)
            if balanced[0] is False:
               return 0

            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0
            return max(left_height, right_height) + 1

        height(root)
        return balanced[0]



"""Input: root = [3,9,20,null,null,15,7]
Output: true"""

solution = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

bbt = solution.isBalanced(root)
print(bbt)



