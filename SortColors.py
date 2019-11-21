# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.

# 1. count the elem and then replace.
# Time: O(N)

# 2. Use two pointers. Let zero and two record the location of "0" and "2" respectively.
# Time: O(N)

class Solution:
    def sortColors1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 = c1 = c2 = 0
        for elem in nums:
            if elem == 0:
                c0 += 1
            elif elem == 1:
                c1 += 1
            else:
                c2 += 1
        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, l, two = 0, 0, len(nums)-1
        while l <= two:
            if nums[l] == 0:
                nums[zero], nums[l] = nums[l], nums[zero]
                zero += 1
                l += 1
            elif nums[l] == 2:
                nums[two], nums[l] = nums[l], nums[two]
                two -= 1
            else:
                l += 1