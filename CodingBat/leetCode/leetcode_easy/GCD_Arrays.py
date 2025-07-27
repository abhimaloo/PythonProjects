import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        smallest = min(nums)  #We need to compute the GCD of the smallest and largest numbers in the list — so we find those first.
        largest = max(nums)
        return gcd(smallest, largest)  #Step 2: The gcd(a, b) function

"""
Given an array of integers nums, return the Greatest Common Divisor (GCD) of the smallest and largest numbers in the array.
Explanation:

Smallest number = 2
Largest number = 10
GCD(2, 10) = 2 ✅
 Approach
Find the minimum and maximum values in the array.
Use the Euclidean algorithm to compute the GCD:
gcd(a, b) = gcd(b, a % b) until b == 0.

Why Use While Loop?
Because:
We keep replacing (a, b) with (b, a % b)
This repeats until b becomes 0
The last non-zero a is the GCD

 Time and Space Complexity
Time: O(n) to find min and max + O(log(min)) for GCD

Space: O(1)

"""