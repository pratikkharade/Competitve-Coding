# Leetcode 0007
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0
        n = abs(x)
        res = 0
        while n > 0:
            res = (res * 10) + (n % 10)
            if res > pow(2, 31) - 1 or res < -1 * pow(2, 31) - 1:
                return 0
            n = n // 10

        if isNeg:
            return -1 * res
        return res