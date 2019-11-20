# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.

# 1. Since we loop from the beginning, if nums[i] < nums[i-1], before that, we have nums[i-1] > nums[i-2]. Thus, i-1 is a peak.
# Else, the len(nums)-1 will be a peak, since nums[len(nums)-1] > nums[len(nums)-2].
# Time complexity: O(N)

# 2. Binary Search
# Time complexity: O(NlogN)


class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i - 1
        return len(nums) - 1


    def findPeakElement2(self, nums: List[int]) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            if l == r:
                return l
            mid = (l + r)//2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return mid