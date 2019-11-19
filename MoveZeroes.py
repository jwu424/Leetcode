# Move Zeroes. 
# Given an array num, move all 0 to the end of it while maintaining the relative order of the non-zero elements.

# For the first solution, Looping i, each time when we get a non-zeor value, we set nums[z]=nums[i] and z += 1. Later, set rest part to 0.
# Time complexity: O(n)

# For the second solution, consider i and j as two pointers. Looping j and each time we find nums[j] != 0, we switch nums[i] and nums[j] and set i += 1
# Time complexity: O(n). But faster than the first one.


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[z] = nums[i]
                z += 1
        for i in range(z, len(nums)):
            nums[i] = 0
    

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1