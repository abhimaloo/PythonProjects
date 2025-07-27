
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # where to write in the chars list
        read = 0   # current position reading characters

        while read < len(chars):
            ch = chars[read]
            count = 0

            # Count occurrences of the same char
            while read < len(chars) and chars[read] == ch:
                read += 1
                count += 1

            # Write the character
            chars[write] = ch
            write += 1

            # Write the count if more than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

"""
Given a list of characters, compress it in-place using the following rules:
Repeated characters are replaced with the character followed by the count (if count > 1)
The new length must be returned
You must modify the input array in-place with O(1) extra space

Use two pointers:
read pointer to go through the input
write pointer to overwrite compressed characters into the original array


"""