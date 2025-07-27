class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0  # pointer for where the next 0 should go
        r = len(nums)-1  # pointer for where the next 2 should go
        i = 0    # current index being scanned


        #Swaps two elements in the array. Used to put 0s and 2s in the correct place.
        def swap (i, j):
            temp = nums[i]
            nums[i]= nums[j]
            nums[j] = temp

        while i <= r:  # We only process elements up to r, because anything after r is already a 2 (sorted).
            if nums[i] == 0:
                swap(l, i)
                l+=1
            elif nums[i]==2 :
                swap (i, r)
                r-=1
                i-=1   # After swapping, the new value at i could still be 0, 1, or 2
            i+=1   #So we re-check it on the next loop (since i will increment again after this)


"""
Time	O(n) — one pass through the list
Space	O(1) — in-place sorting"""