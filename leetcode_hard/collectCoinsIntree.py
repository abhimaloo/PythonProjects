from collections import defaultdict, deque

"""using a tree pruning + BFS/topological sort approach:
🧰 Core Idea
Prune leaf nodes with no coins, repeatedly, because they’re irrelevant to collecting anything.

Prune two additional layers of nodes outward from leaves (since each move lets you collect coins within distance 2).

Count the remaining edges—each remaining edge must be traversed twice (back & forth). 💡using a tree pruning + BFS/topological sort approach:

🧰"""

class Solution:
    def collectTheCoins(self, coins, edges):
        n = len(coins)
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Step 1: Remove all coinless leaves
        queue = deque(i for i in range(n) if len(graph[i]) == 1 and coins[i] == 0)
        while queue:
            u = queue.popleft()
            if not graph[u]:
                continue
            v = graph[u].pop()
            graph[v].remove(u)
            if coins[v] == 0 and len(graph[v]) == 1:
                queue.append(v)

        # Step 2: Prune two layers of leaves
        for _ in range(2):
            leaves = [i for i in range(n) if len(graph[i]) == 1]
            for u in leaves:
                v = graph[u].pop()
                graph[v].remove(u)

        # Step 3: Count remaining edges
        remaining_edges = sum(len(adj) for adj in graph.values()) // 2
        return remaining_edges * 2

"""Step-by-Step Explanation
Build adjacency list for the tree.

Initialize queue with leaves (deg == 1) that have no coins.

Iteratively prune these leaves:

Remove the leaf and its edge.

If this creates a new coinless leaf, add it to the queue.

After pruning all irrelevant parts, prune two more layers:

These might now be leaves but still part of range-2 reachable regions; removing them ensures we don’t overcount edges we don’t need to traverse.

Count edges still remaining in the pruned tree:

Each edge is counted twice (once forward, once back), so multiply by 2.

⏱️ Time & Space Complexity
Time Complexity: O(n)
Every node and edge is processed a constant number of times (initial build, leaf pruning, 2 layers pruning).

Space Complexity: O(n)
Adjacency list, queue, and temporary lists all use O(n).

🧠 Intuition Recap
Leaf-pruning reduces the tree to just the “essential core” where collecting coins is possible.

Two-layer pruning accounts for the collection range of 2, ensuring you only traverse the truly needed edges.

The remaining edges in this core are those you need to walk in both directions → answer = remaining_edges * 2.

"""