class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a = 0
        b = 1

        for _ in range(2, n + 1):
            temp = b
            b = a + b
            a = temp

        return b
