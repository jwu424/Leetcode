# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.


# 1. Sort the nums and try to find the majority element.
# Time complexity: O(NlogN)

# 2. Sort the nums and try to find the majority element.
# Time complexity: O(NlogN)

# 3. Using dictionary to store the count and then find the majority element.
# Time complexity: O(N)

# 4. Consider a pair of elements from the list, if not same, we delete them and the remaining element will be majority one.
# Time conplexity: O(N)

class Solution:
    def majorityElement1(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]
        nums.sort()
        count = 0
        temp = nums[0]
        for i in range(len(nums)):
            if nums[i] == temp:
                count += 1
            else:
                if count > len(nums)//2:
                    return temp
                else:
                    temp = nums[i]
                    count = 1
        return temp

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement3(self, nums: List[int]) -> int:
        dictt = {}
        for elem in nums:
            dictt[elem] = dictt.get(elem, 0) + 1
        for key, count in dictt.items():
            if count > len(nums)//2:
                return key

    def majorityElement4(self, nums: List[int]) -> int:
        count, cand = 0, 0
        for num in nums:
            if num == cand:
                count += 1
            elif count == 0:
                count, cand = 1, num
            else:
                count -= 1
        return cand