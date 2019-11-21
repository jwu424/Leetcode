# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.


# 1. The maximum index can be reached for current elem is num[i]+i.
# Create a maxJump = max(maxJump, num[i]+i)
# Time: O(N)




class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        for i in range(len(nums)):
            if i > maxJump:
                return False
            maxJump = max(maxJump, nums[i] + i)
        return True