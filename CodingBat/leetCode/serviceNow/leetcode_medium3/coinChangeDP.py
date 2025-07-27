class Solution:
    def coinChange(self, coins, amount):
        coins.sort()
        memo = {0:0}

        def min_coins(amt):
            if amt in memo:
                return memo[amt]

            minn = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                minn = min(minn, 1 + min_coins(diff))
            memo[amt] = minn
            return minn

        result = min_coins(amount)
        if result < float('inf'):
            return result
        else:
            return -1

"""
Sort coins to allow early stopping when coin > amount
memo is a dictionary used for memoization (caching subproblem results)
memo[amt] will store the minimum number of coins needed for amount amt
We initialize memo[0] = 0, meaning 0 coins are needed to make amount 0.
If we’ve already solved the subproblem amt, return it directly (to avoid recomputation)
Try every coin that doesn’t exceed amt
diff = amt - coin is the remaining amount after choosing this coin
Recursively compute min_coins(diff)
minn keeps track of the min
Store minn in memo[amt] so we don’t recompute it later
Time Complexity
Worst-case: O(amount × len(coins))
Each amount from 1 to amount is computed once
Each computation checks up to len(coins) coins
📦 Space Complexity
O(amount) for the memoization dictionary


"""

solution = Solution()
coins = [1, 2, 5]
amount = 11
print(solution.coinChange(coins, amount))











