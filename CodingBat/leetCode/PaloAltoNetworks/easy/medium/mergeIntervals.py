"""
You are given a list of intervals [[start1, end1], [start2, end2], ...].
Merge all overlapping intervals and return the result as a new list.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        intervals.sort(key=lambda i: i[0])   # Sort intervals based on the start time (first element of each sublist).
        output = [intervals[0]]   #  Initialize output list with first interval

        for start, end in intervals[1:]:  #Loop through all intervals starting from the second one.
            lastend = output[-1][1]   #lastend is the end of the last interval in the output.

# Merge if Overlapping
            if start <= lastend:
                output[-1][1] = max(end, lastend)
            else:
                output.append([start, end])
        return output

"""
Sort intervals based on their start time.
This ensures that any potential overlaps will be next to each other.
Start with the first interval in the result list (output).

If the current interval overlaps with the last interval in output (i.e., start <= lastend):
Merge them by updating the end of the last interval to the maximum of current end and lastend.

➕ Step 5: No Overlap → Add New Interval
If there's no overlap, just add the current interval to the result.
Return the final merged list.



🔁 Example:
Input:


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Sorted:

[[1, 3], [2, 6], [8, 10], [15, 18]]
Merging Steps:

[1, 3] and [2, 6] → merged to [1, 6]

[1, 6] and [8, 10] → no overlap → add [8, 10]

[8, 10] and [15, 18] → no overlap → add [15, 18]

Output:

[[1, 6], [8, 10], [15, 18]]







 Time and Space Complexity
Aspect	Complexity
Time	O(n log n) — for sorting the intervals
O(n) — to iterate and merge
Total	O(n log n) overall
Space	O(n) — for the output list



"""