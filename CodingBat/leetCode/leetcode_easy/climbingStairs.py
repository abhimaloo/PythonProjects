#Time Complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range (n-1):
           temp = one
           one = one + two
           two = temp

        return one


"""explanation:
one represents f(i+1) — the number of ways to reach step i+1

two represents f(i) — the number of ways to reach step i

You iterate from 0 to n-2 (i.e., n-1 times total), which builds up the result using the Fibonacci recurrence."""