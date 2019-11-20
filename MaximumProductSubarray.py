# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# 1. multiply from left to right and right to left
# Time complexity: O(N); Space: O(N)

# 2. create locMin, locMax, gloMax to record the situation of each step.
# Time complexity: O(N); Space: O(1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        inv = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            inv[i] *= inv[i-1] or 1
        return max(nums + inv)

    def maxProduct2(self, nums: List[int]) -> int:
        if not nums:
            return 
        locMin = locMax = gloMax = nums[0]
        for i in range(1, len(nums)):
            temp = locMin
            locMin = min(locMin*nums[i], nums[i], locMax*nums[i])
            locMax = max(temp*nums[i], nums[i], locMax*nums[i])
            gloMax = max(gloMax, locMax)
        return gloMax