"""
A string can be abbreviated by replacing any number of non-adjacent,
non-empty substrings with their lengths. The lengths should not have leading zeros.
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

"""

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False

                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num

            else:
                if word[i] != abbr[j]:
                    return False
                else:
                    i += 1
                    j += 1
        return i == len(word) and j == len(abbr)























