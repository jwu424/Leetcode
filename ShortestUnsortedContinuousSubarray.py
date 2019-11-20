# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.

# 1. sort the nums and compare the sorted nums with nums from beginning and end.
# Time complexity: o(NlogN)

# 2. Start from left, try to find the maximum. If nums[i] < max, then left part of i need to be sorted.
# Start from right, try to find the minimum. If nums[i] > min, then the right part of i need to be sorted.
# Time complexity: O(N)

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_num = sorted(nums)
        l1, l2 = 0, len(nums)-1
        while l1 <= l2 and nums[l1] == sorted_num[l1]:
            l1 += 1
        while l1 <= l2 and nums[l2] == sorted_num[l2]:
            l2 -= 1
        return l2 - l1 + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        l_max = nums[0]
        l = 0
        for i in range(len(nums)):
            if nums[i] > l_max:
                l_max = nums[i]
            elif nums[i] < l_max:
                l = i
        r_min = nums[-1]
        r = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < r_min:
                r_min = nums[i]
            elif nums[i] > r_min:
                r = i
        if r >= l:
            return 0
        return l - r + 1