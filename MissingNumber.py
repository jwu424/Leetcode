# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.

# First, using math. compare sum of nums with sum of range(len(nums)+1), since
# we know there is one missing value.
# Time complexity: O(n)

# Second, sort the nums and then compare the value of nums with its index. 
# Time complexity: O(nlog(n))


class Solution:
    def missingNumber1(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
        # return len(nums)*(len(nums)+1)//2 - sum(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)