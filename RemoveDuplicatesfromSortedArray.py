# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# 1. Since the array is sorted, we can compare current one with previous one, if not same, rewrite the record position with current one.
# Time complexity: O(n)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[index] = nums[i]
                index += 1
        return index