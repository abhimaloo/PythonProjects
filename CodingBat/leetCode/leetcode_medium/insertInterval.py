class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for i in range (len(intervals)):
            #Case 1: New interval is before current interval — no overlap
            if newInterval[1] < intervals[i][0] :
                result.append(newInterval)
                return result + intervals[i:] # Append newInterval, then add the remaining intervals and return.
            elif newInterval[0] > intervals[i][1]: #New interval is after current interval — no overlap
                result.append(intervals[i])
            else:   #Overlap — merge with current interval
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        #If we never returned inside the loop,
        # it means the newInterval comes at the end or was merged all along. So append it now and return.
        result.append(newInterval)
        return result

"""Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

"""
Time Complexity: O(n)
Every interval is checked once.

📦 Space Complexity: O(n)"""

sol = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(sol.insert(intervals, newInterval))