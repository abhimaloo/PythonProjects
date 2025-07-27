class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        self.prev = None
        self.head = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)

            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                self.head = node

            self.prev = node
            dfs(node.right)

        dfs(root)

        # Circular connection
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head


"""
✅ Problem:
Convert a BST into a sorted circular doubly linked list in-place (reusing the tree's nodes), such that:
The left pointer is the previous node.
The right pointer is the next node.

✅ Key Idea:
Use in-order traversal, because it visits nodes in sorted order for BSTs.
Maintain:
prev: The previously visited node.
head: The smallest (first) node in the list.
As you visit each node:
Link it with prev
Update prev to the current node
"""