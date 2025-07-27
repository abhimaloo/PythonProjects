class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count_ones = 0
        time = 0

        for ch in s:
            if ch == '1':
                count_ones += 1
            elif ch == '0' and count_ones > 0:
                time = max(time + 1, count_ones)

        return time
"""

Problem Statement:
You are given a binary string s (consisting only of '0' and '1').

In one second, all occurrences of the substring '01' can be simultaneously replaced with '10'.

Return the number of seconds needed to transform the string into a state where no more '01' 
substrings exist (i.e., all '1's are to the left of all '0's).

Approach: Greedy Simulation with Count Tracking
Instead of simulating the entire string, we track:

How many 1s we've seen so far.

How many seconds (moves) it takes for each '0' to "pass through" all the '1's to its left.

Each '0' needs to move past the '1's to its left. But '0's can’t move past more than 
one '1' in a single second unless there are gaps.

So we maintain:

count_ones: how many '1's we've seen.

time: the minimum number of seconds required so far.


Rule:
When we see a '0', it will need at least count_ones moves to get to the right side of all the '1's.


But we also need to wait for earlier zeros to finish their moves, 
so we set time = max(time + 1, count_ones).



"""