# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.


# 1. Brute force
# Time: O(N)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 1
        for i in range(len(digits)-1, -1, -1):
            if temp == 0:
                break
            if i == 0 and (digits[0] + temp == 10):
                digits[i] = 0
                digits = [1] + digits
                continue
            cur = temp + digits[i]
            digits[i] = cur % 10
            temp = cur // 10
        return digits

