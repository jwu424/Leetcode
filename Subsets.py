# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.


# 1. DFS
# Time: O(2^N)

# 2. Iteratively
# Time: O(2^N)

class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, start, temp, res):
        res.append(temp)
        for i in range(start, len(nums)):
            self.dfs(nums, i+1, temp+[nums[i]], res)

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for elem in nums:
            res += [[elem] + temp for temp in res]
        return res