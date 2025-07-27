from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = {}

        def dfs(crs):  # DFS Function
            if crs in visitSet:
                return False  # If the current course is already being visited, then a cycle exists.
            if preMap[crs] == []:
                return True  # no prereq or already processed
            visitSet.add(crs)  # Mark course as visited (in the stack).

            for pre in preMap[crs]:  # Recursively DFS on all prerequisites.
                if not dfs(pre):
                    return False
            visitSet.remove(crs)   # Remove from set once all pre-reqs are successfully verified.
            preMap[crs] = []  # Empty the prerequisites list for memoization to skip future redundant DFS.
            return True

        for crs in range(numCourses):    #  Run DFS on every course
            if not dfs(crs):              # If any DFS detects a cycle, return False.
                return False
        return True

"""
preMap maps each course to its list of prerequisites.
visitSet keeps track of nodes currently in the DFS call stack.
Used to detect cycles: if we revisit a node already in visitSet, there's a cycle.

If a course has no prerequisites, it's "safe" to take.

Time and Space Complexity
Time Complexity: O(N + E)

N = number of courses, E = number of prerequisites

Each course and edge is visited once

Space Complexity: O(N + E)

For preMap, recursion stack, and visitSet

"""