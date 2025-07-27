
class Solution:
  def threeSum(self, nums):
    result = []
    nums.sort()
    n = len(nums)

    for i in range (n):
        if nums[i] > 0 :
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        lo , hi  = i+1 , n-1
        while lo < hi:
            summ = nums[i] + nums[lo]+ nums[hi]
            if summ == 0:
                result.append([nums[i],nums[lo], nums[hi]])
                lo+=1
                hi-=1

                while lo < hi and nums[lo] == nums[lo-1]:
                    lo+=1
                while lo < hi and nums[hi] == nums[hi+1]:
                    hi-=1

            elif summ < 0:
                lo+=1
            else:
                hi-=1

    return result


# Execution
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))

"""
Time and Space Complexity:
Time: O(n^2)
Outer loop: O(n)
Two-pointer scan inside: O(n)
→ Total: O(n^2)

Space:
Total Space Complexity:
O(log n + k)
Where:

log n is due to sorting
k is the number of triplets in the result

"""










