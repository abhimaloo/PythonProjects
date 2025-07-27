class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Position to write compressed char
        read = 0  # Position to read original chars

        while read < len(chars):
            current_char = chars[read]
            count = 0

            # Count duplicates
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            # Write the character
            chars[write] = current_char
            write += 1

            # Write the count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

"""
Approach:
Use two pointers:
write to write compressed characters.
read to traverse input.
Count consecutive repeated characters.
Write the character once.
If count > 1, write the count digits.

Time Complexity:
O(n) — single pass through the array

📦 Space Complexity:
O(1) — in-place compression


"""