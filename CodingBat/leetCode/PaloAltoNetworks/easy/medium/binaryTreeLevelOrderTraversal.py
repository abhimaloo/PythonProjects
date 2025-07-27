import collections
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root):
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result

"""
Binary tree level order traversal, also known as Breadth-First Search (BFS) traversal, is a method of visiting all nodes of a binary tree level by level, starting from the root. 
It processes all nodes at a given depth before moving on to the next depth level.

result: Stores the final list of levels.

q: A queue (double-ended queue) for BFS traversal.

The root is added to the queue to start.

qlen is the number of nodes at the current level.

level stores the values of the current level's nodes.

Process all nodes in the current level:

Take each node out of the queue and process it.
Add its value to the level list.

Enqueue its left and right children (even if they are None, which will be skipped later).
Time Complexity: O(n)
Every node is visited exactly once.

Space Complexity: O(n)
For the queue and result list — in the worst case (e.g., full binary tree), up to n/2 nodes may be in the queue at once.



"""















