from collections import defaultdict, deque
class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        graph = defaultdict(list)

        # Step 1: Build graph using DFS
        def buildGraph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root, None)

        # Step 2: BFS from the start node
        visited = set()
        queue = deque()
        queue.append(start)
        visited.add(start)
        time = -1  # Starts from -1 so first layer becomes 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            time += 1  # Each layer = 1 second

        return time
"""
 Problem Statement:
You are given the root of a binary tree, and an integer start.
At time t = 0, the node with value start gets infected.
Every second, the infection spreads from any infected node to its children and parent.
Return the total time it takes to infect the entire tree.
🧠 Key Insight:
This is a graph problem on a binary tree. Each node is a vertex, and edges exist between:
Parent → Left child
Parent → Right child
Child → Parent (we must add this manually since binary tree nodes don’t store parent)
Approach:
Step 1: Build a Graph
Use BFS or DFS to build an adjacency list that connects:
Node ↔ Left child
Node ↔ Right child
Node ↔ Parent
Step 2: BFS from start node
Treat the graph as an undirected graph.
Perform BFS from start and count how many levels (seconds) it takes to reach all nodes.
Explanation:
Graph Creation: We connect each node to its parent and children to allow bidirectional traversal.
BFS: Each level of BFS represents the spread of infection to the next layer.
We return the number of layers (seconds) it took to infect all nodes.
⏱ Time Complexity:
O(n) — Visit each node once.
O(n) — For building the graph and BFS traversal.
📦 Space Complexity:
O(n) — For graph and BFS queue.
"""