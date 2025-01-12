# Leetcode 0342
# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0 or n == 1:
            return bool(n)
        if n % 4 != 0:
            return False
        return self.isPowerOfFour(n // 4)