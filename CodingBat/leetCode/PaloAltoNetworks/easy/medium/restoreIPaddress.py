class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start=0, path=[]):
            # If we already have 4 parts and we're at the end of the string
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return

            for length in range(1, 4):  # segment can be 1 to 3 digits
                if start + length > len(s):
                    break

                segment = s[start:start+length]

                # Skip invalid segments
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue

                backtrack(start + length, path + [segment])
                #Move forward length characters
                #Add current segment to the path

        backtrack()
        return result


"""
Each IP address must have:
Exactly 4 parts (segments)
Each part in 0–255
No leading zeros (e.g., "01" is invalid, but "0" is valid)

A helper function that tries to:
Start from start index
Build up the path (partial IP parts)


If you have 4 parts:
✅ Only add to result if you've also used up all digits
❌ If not at end → return without doing anything

 Time Complexity
O(1): The string has at most 12 digits (each segment ≤ 3 digits), so total combinations are bounded
Practically backtracking is very efficient due to pruning:
Skips invalid segments early
Stops at 4 segments
"""