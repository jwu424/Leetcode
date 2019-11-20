# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# 1. Use dictionary to store.
# Time complexity: O(N)

#2. Two pointers. Since we need to return index, we should use zip and sort the pair.
# Then, the rest is the Binary Search.
# Time complexity: O(NlogN)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i, num in enumerate(nums):
            if target-num in dictt:
                return (dictt[target-num], i)
            dictt[num] = i

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        l = sorted(zip(nums, range(len(nums))))
        left, right = 0, len(nums)-1
        while left < right:
            temp = l[left][0] + l[right][0]
            if target == temp:
                return l[left][1], l[right][1]
            elif target < temp:
                right -= 1
            else:
                left += 1