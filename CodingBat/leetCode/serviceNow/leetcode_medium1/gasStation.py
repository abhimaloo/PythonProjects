"""
greedy o(n)
"""
"""
A greedy algorithm is a problem-solving strategy where you:

Make the locally optimal choice at each step, hoping it leads to a globally optimal solution.

In simpler terms:
You grab what looks best right now, without worrying about future consequences."""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        """If the total gas is less than the total cost, it is impossible to complete the trip. 
        This is a greedy global filter — quickly eliminate all cases where a solution can't exist."""

        total = 0
        result = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                result = i + 1

                """As you iterate, if the gas tank goes negative (total < 0), 
                you know none of the stations from the last result up to i can be the start.

          So you greedily pick the next station (i+1) as a better candidate and reset."""

        return result

#If the loop finishes, then result is a valid starting index.

