class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people  # Initialize a list with 0 for each person
        i = 0                   # This keeps track of the turn
        give = 1                # This is the number of candies to give in the current turn

        while candies > 0:
            res[i % num_people] += min(give, candies)  # Add candies to the correct person
            candies -= give                            # Subtract given candies from total
            give += 1                                  # Increase the amount to give next
            i += 1                                     # Move to next person (or next round)

        return res




"""
You have:
candies — the total number of candies.
num_people — the number of people standing in a line.
Distribute the candies as follows:
Start from the first person.
Give 1 candy to the first person, 2 to the second, and so on.
After the last person, start from the beginning again, increasing the count by 1 each time.
If candies run out before giving the expected amount, give them the remaining candies.
Return a list of length num_people representing how many candies each person gets.

Example
Input:
candies = 10
num_people = 3
Output:
[5, 2, 3]
Explanation:
Round 1: [1, 2, 3] → total 6 → remaining 4
Round 2: [4, - , -] → remaining 0
Final: [5, 2, 3]

Time & Space Complexity
Time: O(√candies) — because 1 + 2 + 3 + ... + k ≈ candies, so loop runs ~ √candies times.

Space: O(num_people)

Great question!

When we say the time complexity is O(√candies) in the solution for 
Leetcode 1103 (Distribute Candies to People), 
we’re referring to the number of steps the algorithm takes before it stops 
— in terms of the input size candies.



"""