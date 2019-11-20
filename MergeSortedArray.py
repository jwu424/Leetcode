# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

# 1. Better to replace from the end of two lists. 
# Note: we should be careful when nums1 doesn't have elements.
# Time complexity: O(N)



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        f, s, end = m-1, n-1, m+n-1
        while f >= 0 and s >= 0:
            if nums1[f] < nums2[s]:
                nums1[end] = nums2[s]
                s -= 1
            else:
                nums1[end] = nums1[f]
                f -= 1
            end -= 1
        if f < 0:
            nums1[:s+1] = nums2[:s+1]