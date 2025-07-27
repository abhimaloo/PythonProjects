from collections import defaultdict

# time cpmplexity =O(n×d)
#n = highLimit - lowLimit + 1
#d = number of digits in each number (at most 6 for inputs ≤ 10⁵)
#Space: O(k) — where k is the number of unique digit sums (at most 54 for 99999 → 9+9+9+9+9 = 45)

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = defaultdict(int)

        def digitSum(n):  #Converts the number to a string, and then adds all its digits.
            return sum(int(d) for d in str(n))

        for i in range (lowLimit, highLimit+1):   #For each ball number between lowLimit and highLimit (inclusive):
            box = digitSum(i)                      #Compute its digit sum to find the box
            count[box] += 1                       #Add 1 to that box's count
        return max(count.values())
