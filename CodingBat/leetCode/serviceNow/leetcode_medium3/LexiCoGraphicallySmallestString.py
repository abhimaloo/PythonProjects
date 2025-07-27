class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def distance(c1, c2):
            return min(abs(ord(c1) - ord(c2)), 26 - abs(ord(c1) - ord(c2)))

        res = []
        for ch in s:
            for target in range(26):  # from 'a' to 'z'
                new_char = chr(ord('a') + target)
                cost = distance(ch, new_char)
                if cost <= k:
                    res.append(new_char)
                    k -= cost
                    break  # move to next character
        return ''.join(res)
"""
 Understanding the problem
 You're given:
A lowercase string s , An integer k
Your task is to transform s into the lexicographically smallest possible string, by changing characters.
Each change has a cost:
You can change any character c1 to c2
The cost is the minimum number of steps needed to convert c1 to c2 in the circular alphabet (wraps around from 'z' to 'a')

Key Rule:
The circular distance between two characters c1 and c2 is:
min(abs(ord(c1) - ord(c2)), 26 - abs(ord(c1) - ord(c2)))
This ensures wrap-around is accounted for.
Goal:
Convert s into the smallest possible string (lexicographically) by spending at most k total cost.

For each character ch in s:
Try to replace it with the smallest possible letter ('a' to 'z')
Check how much it would cost (distance(ch, new_char))
If that cost is within the remaining budget k, apply the change:
Append the new character
Subtract cost from k
Break out of loop (move to next character)


It's a very common Python idiom used to generate characters dynamically, 
especially when looping through the alphabet.

🔍 Step-by-Step Breakdown
1. ord('a')
This gives you the ASCII value (Unicode code point) of the character 'a'.

'a' → ASCII 97

2. ord('a') + target
target ranges from 0 to 25 in your loop:


for target in range(26):  # 0 to 25
So this expression generates numbers from:

97 + 0 = 97 → 'a'

97 + 1 = 98 → 'b'

...

97 + 25 = 122 → 'z'

3. chr(...)
chr() takes an ASCII (Unicode) value and returns the character.
So chr(97) = 'a', chr(98) = 'b', ..., chr(122) = 'z'
✅ So what does it do?

new_char = chr(ord('a') + target)
It converts a number from 0 to 25 into the corresponding lowercase letter of the English alphabet.

💡 Example:
If target = 3:

ord('a') + 3 = 100
chr(100) = 'd'
→ new_char = 'd'

"""