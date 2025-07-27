class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        time = 0

        while True:
            i = 0
            changed = False
            while i < len(s) - 1:
                if s[i] == '0' and s[i + 1] == '1':
                    # Swap "01" → "10"
                    s[i], s[i + 1] = '1', '0'
                    i += 2  # Skip next because we can't double swap
                    changed = True
                else:
                    i += 1
            if not changed:
                break
            time += 1

        return time

"""
Correct Approach: Simulation
We simulate each second:
Scan the string for "01" pairs.
Replace them with "10" (simultaneously).
Repeat until no more changes.

✅ Example Walkthrough
Input: "0110101"

t=0: "0110101"
t=1: "1011010"
t=2: "1101100"
t=3: "1110100"
t=4: "1111000" ← Done
Output: 4

Time Complexity
Time: O(n²) in worst case (n swaps per time step and up to n time steps)

Space: O(n) (we convert string to list to allow in-place swaps)



"""