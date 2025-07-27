
class Solution:
    def minOperations(self, n: int) :
        queue = deque([(n, 0)])
        visited = set([n])

        while queue:
            current , steps = queue.popleft()
            if (current == 0):
                return steps

           # calculate power
            for i in range (20):
                power = 2 ** i
                for next_value in [current + power , current - power]:
                 if 0 <= next_value <= 2 * n  and next_value not in visited:
                    queue.append((next_value, steps + 1))
                    visited.add(next_value)


"""
What the Code Does:
Uses a queue to store pairs (current_value, steps_taken).

Starts from n.

For each state, tries to add or subtract powers of two 
If it reaches zero, returns the number of steps.
Uses a visited set to avoid repeated states.
Limits next states to be within [0, 2*n] to avoid infinite expansion.
Explanation of the approach:
This BFS finds the shortest path (minimum operations)
from n to 0 where each operation is adding or subtracting a power of two.

"""




















