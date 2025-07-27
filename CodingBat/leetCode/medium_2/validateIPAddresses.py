class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3 and self.isIPv4(queryIP):
            return "IPv4"
        elif queryIP.count(':') == 7 and self.isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"

    def isIPv4(self, ip: str) -> bool:
        parts = ip.split('.')
        if len(parts) != 4:
            return False

        for part in parts:
            # Check empty string or leading zeros
            if not part or (part[0] == '0' and len(part) > 1):
                return False

            if not part.isdigit():
                return False

            num = int(part)
            if num < 0 or num > 255:
                return False

        return True

    def isIPv6(self, ip: str) -> bool:
        parts = ip.split(':')
        if len(parts) != 8:
            return False

        hex_digits = '0123456789abcdefABCDEF'
        for part in parts:
            if not 1 <= len(part) <= 4:
                return False
            if not all(ch in hex_digits for ch in part):
                return False

        return True

"""
🧠 Summary:
Validate IPv4 by checking 4 parts, numeric, no leading zeros, and 0 ≤ val ≤ 255.
Validate IPv6 by checking 8 parts, hex digits only, length 1 to 4.
Time Complexity:
O(n), where n is length of input string (split and check each part).
📦 Space Complexity:
O(1), constant space for checking parts.


"""