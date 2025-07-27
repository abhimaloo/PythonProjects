class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False


"""
Time Complexity: O(n)
Each lookup (n in hashset) and insert (hashset.add(n)) is O(1) on average.

So total time is O(n) for n elements.

📦 Space Complexity: O(n)
In the worst case (no duplicates), we store all n elements in the set.

"""
