class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])  # Sort by start time

        for i in range(1, len(intervals)):
            prev_end = intervals[i - 1][1]  ## end time of previous meeting
            curr_start = intervals[i][0]    ## start time of current meeting
            if curr_start < prev_end:
                return False  # Overlap found

        return True  # No overlaps


"""
If two meetings overlap, the person cannot attend both.
So:
Sort intervals by start time.
Check each interval:
We sort the meetings by their start time, 
so we can easily detect if any meeting starts before the previous one ends.
If current start < previous end → there's an overlap → return False.


Time Complexity:
O(n log n) → for sorting

O(n) → for checking overlaps
"""