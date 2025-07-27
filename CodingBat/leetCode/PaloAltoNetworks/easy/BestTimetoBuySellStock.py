from typing import List

# time cmplexity o (n)
class Solution:
    def maxProfit(prices) :
        min_price = float('inf')  # The lowest price seen so far
        max_profit = 0            # The highest profit seen so far

        for price in prices:
            if price < min_price:
               min_price = price         # Update lowest price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit    # Update max profit

        return max_profit

"""
You're given a list prices, where each element represents the stock price on a given day.
You must buy before you sell and can complete only one transaction.
Your goal is to calculate the maximum profit you could have made.

Walkthrough:

Day 0: 7 → min = 7
Day 1: 1 → min = 1
Day 2: 5 → profit = 4 → max_profit = 4
Day 3: 3 → profit = 2 → max_profit = 4
Day 4: 6 → profit = 5 → max_profit = 5 ✅
Day 5: 4 → profit = 3 → max_profit = 5


"""