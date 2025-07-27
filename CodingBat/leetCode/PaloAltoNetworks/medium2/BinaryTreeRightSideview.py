# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qlen = len(q)

            for i in range (qlen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                result.append(rightSide.val)
        return result

"""
It returns a list of node values you'd see if you looked at the tree from the right side — 
i.e., the rightmost node at each level.

result will hold the rightmost node's values for each level.
q is a queue initialized with the root node — this will help us do a level order traversal (BFS).
While there are nodes to process in the queue:

rightSide will track the last node processed at the current level.

qlen is the number of nodes at this current level.
Process all nodes in the current level (qlen times):
Pop node from the queue.

If it's not None:
Update rightSide to the current node (the last non-null node encountered at this level).
Add the node's left and right children to the queue for the next level.

After processing the whole level, add the value of the rightmost node (rightSide) to result.
Returns the list of rightmost node values for all levels.

Metric	Value
Time	O(N), all nodes visited once
Space	O(N), for queue in worst case
"""