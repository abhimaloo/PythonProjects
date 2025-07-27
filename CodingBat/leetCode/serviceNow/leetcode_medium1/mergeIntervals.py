class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        intervals.sort(key=lambda i: i[0])   # Sort intervals based on the start time (first element of each sublist).
        output = [intervals[0]]   #  Initialize output list with first interval

        for start, end in intervals[1:]:  #Loop through all intervals starting from the second one.
            lastend = output[-1][1]

            if start <= lastend:
                output[-1][1] = max(end, lastend)
            else:
                output.append([start, end])
        return output






"""
 Time and Space Complexity
Aspect	Complexity
Time	O(n log n) — for sorting the intervals
O(n) — to iterate and merge
Total	O(n log n) overall
Space	O(n) — for the output list



"""