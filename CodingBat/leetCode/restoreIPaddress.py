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

        backtrack()
        return result