
# time cmplexity o(n)

def twoSum(nums, target):
    num_container = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_container:
            return num_container[complement], i
        else:
            num_container[num] = i

    return []





def twoSum(nums, target):
    num_container = {}

    for i, num in enumerate(nums):
        complement = num - target

        if complement in num_container:
            return num_container[complement], i
        else:
            num_container[num] = i
    return []