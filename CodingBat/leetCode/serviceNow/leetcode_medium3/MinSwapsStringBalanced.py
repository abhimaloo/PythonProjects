class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_imbalance = 0

        for c in s:
            if c == '[':
                balance += 1
            else:  # c == ']'
                balance -= 1

            # track how negative balance goes
            if balance < 0:
                max_imbalance = max(max_imbalance, -balance)

        # Minimum swaps needed is ceil(max_imbalance / 2)
        return (max_imbalance + 1) // 2
"""
✅ Key Insight:
You don't need to actually perform the swaps.
Instead, count how unbalanced the string is, then compute the minimum swaps needed.
💡 How?
Keep a balance counter:
When you see '[': increment balance
When you see ']': decrement balance
If balance goes negative, it means you have more closing brackets than opening ones — i.e., imbalance.
✅ Minimum Swaps Formula:
If max imbalance is x, then you need (x + 1) // 2 swaps.

Example Dry Run:
Input: s = "]][["
Step-by-step:
] → balance = -1 → max_imbalance = 1
] → balance = -2 → max_imbalance = 2
[ → balance = -1
[ → balance = 0
Max imbalance = 2 → (2 + 1) // 2 = 1 swap needed ✅

✅ Time and Space Complexity:
Time: O(n) – one pass through the string

Space: O(1) – constant space
"""