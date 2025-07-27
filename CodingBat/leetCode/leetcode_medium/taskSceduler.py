from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_heap = [-cnt for cnt in task_counts.values()]  # Max heap using negative values
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # each element: (ready_time, count)

        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1  # do task
                if count != 0:
                    cooldown.append((time + n, count))

            # Check if any task has cooled down
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(max_heap, cooldown.popleft()[1])

        return time

    """
You’re given:

A list of tasks represented by capital letters (e.g., ['A', 'A', 'A', 'B', 'B', 'B'])
An integer n, the cooldown period between two same tasks
You must schedule the tasks so that the same task is at least n intervals apart.
✅ Strategy
Count frequency of each task
Use a max heap to always pick the task with the highest remaining count
Use a cooldown queue to track when a task is available again
Simulate time step-by-step
This is a classic greedy + priority queue problem where you're asked to 
schedule tasks with cooling periods to minimize the total time.
Time and Space Complexity
Time: O(N log N)
N = number of tasks; each push/pop in heap takes log time

Space: O(N)
For heap and cooldown queue


    
    
    """
