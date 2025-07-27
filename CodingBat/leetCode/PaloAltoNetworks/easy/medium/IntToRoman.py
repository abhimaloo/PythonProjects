class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""
        for i in range(len(val)):
            while num >= val[i]:
                num -= val[i]
                roman += syms[i]
        return roman



"""
You are using two lists:
val: integer values in descending order (including special Roman subtractive cases like 900, 400, etc.)
syms: corresponding Roman numeral symbols.
You iterate through each value and repeatedly subtract it from num while appending the symbol to the result string.
"""


