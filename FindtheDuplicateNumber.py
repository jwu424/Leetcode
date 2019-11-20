# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# 1. Sort the nums and compare each elem with previous elem.
# Time complexity: O(NlogN)

# 2. Binary Search. Nums is not sorted, but we can use index to count and compare with mid index.
# Time complexity: O(NlogN)

class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def findDuplicate2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        low = 1
        high = len(nums)
        while low < high:
            mid = low + (high-low)//2
            count = 0
            for x in nums:
                if x <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid+1
        return low