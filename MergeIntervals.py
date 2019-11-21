# Given a collection of intervals, merge all overlapping intervals.

# 1. Create a temp variable and compare each elem with its previous one.
# Time: O(N), Space: O(N)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = []
        temp = intervals[0]
        for elem in intervals[1:]:
            if temp[-1] >= elem[0]:
                temp = [temp[0], max(temp[-1], elem[-1])]
            else:
                res.append(temp)
                temp = elem
        res.append(temp)
        return res
        