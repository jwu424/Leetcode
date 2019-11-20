# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# 1. For each elem in nums[1:], if sum(nums[i] + nums[i-1])>nums[i], then this may be part of the subarry we want.
# Time complexity: O(N)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            maxx = max(maxx, nums[i])
        return maxx

