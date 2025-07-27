
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
from typing import Optional

class Solution:
    def cloneGraph(self, node: 'Node'):
        oldToNew = {}

        def dfs_clone(node):
            if not node:
                return
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs_clone(nei))
            return copy

        return dfs_clone(node)


"""
Base case: if the input node is None, return None.
If we’ve already cloned this node before, return its clone to prevent infinite loops.

Create a copy of the current node (with same value).
Store it in oldToNew so we don’t clone it again.
Recursively clone all neighbors.

Append the cloned neighbors to the current node’s neighbors list.
Return the completed cloned node.
Start DFS from the given node and build the full graph.
Time & Space Complexity:
Time: O(n + m)
n = number of nodes
m = number of edges
Space: O(n) for the oldToNew map and recursion stack




"""



