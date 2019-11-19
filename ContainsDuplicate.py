# Given an array of integers, find if the array contains any duplicates.

# First, we use hash table. That is, using dictionary to store value.
# Time complexity: O(n)

# Second, Use set to delete duplicate value.
# Time complexity: O(n)

class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        dictt = {}
        for elem in nums:
            if elem not in dictt:
                dictt[elem] = 1
            else:
                return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))