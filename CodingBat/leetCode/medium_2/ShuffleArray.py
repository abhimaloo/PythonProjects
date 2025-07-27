import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]  # Store a copy of the original
        self.array = nums[:]     # Working copy to shuffle

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            j = random.randint(i, len(self.array) - 1)
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array


"""

Approach: Fisher-Yates Shuffle (a.k.a. Knuth Shuffle)
This algorithm shuffles an array in-place in O(n) time with uniform randomness.
ow Fisher-Yates Works:
For each index i:

Pick a random index j from [i, n-1]

Swap arr[i] with arr[j]

This ensures all permutations are equally likely.
Operation	Time	Space
Constructor	O(n)	O(n)
reset()	O(n)	O(n)
shuffle()	O(n)	O(1) (excluding result array)

Use Fisher-Yates shuffle to get uniform random results in-place.

Keep a deep copy of the original array to support reset().



"""