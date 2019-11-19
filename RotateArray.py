# Given an array, rotate the array to the right by k steps, where k is non-negative.

# 1. Make sure k < len(nums). We can use slice but need extra space.
# Time complexity: O(n). Space: O(n)

# 2. Each time pop the last one and inset it into the beginning of the list.
# Time complexity: O(n^2)

# 3. Reverse the list three times.
# Time complexity: O(n)


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1