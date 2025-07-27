# time complexity is O(n)

class Solution:
    def majorityElement(self, nums: list) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        max_count = -1
        ans = -1

        for key, value in counter.items():
            if value > max_count:
                max_count = value
                ans = key

        return ans

# execution
nums = [3,2,3]

solution = Solution()

print(solution.majorityElement(nums))


"""
Time Complexity: O(n) — The array is traversed only once.

Space Complexity: O(1) — No extra space is used."""



