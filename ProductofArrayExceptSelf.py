# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# 1. We should be careful about 0. If there are more than two zeros, then the whole output will be zero.
# If there is one 0, all elems in output will be zero except the index of 0 in the nums.
# Time complexity: O(N). Space: O(N)

# 2. times from left to right and then left to right.
# Time complexity: O(N). Space: O(N)



class Solution:
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        total = 1
        zero = []
        for i in range(len(nums)):
            if nums[i] != 0:
                total *= nums[i]
            else:
                zero.append(i)
        if len(zero) >= 2:
            return [0]*len(nums)
        elif len(zero) == 1:
            res = [0]*len(nums)
            res[zero[0]] = total
            return res
        else:
            res = []
            for elem in nums:
                res.append(total//elem)
            return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        temp = 1
        for j in range(len(nums)-2, -1, -1):
            temp *= nums[j+1]
            res[j] += temp
        return res