# Leetcode 0066
# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] += 1
                break
        if carry == 1:
            digits = [1] + digits
        return digits