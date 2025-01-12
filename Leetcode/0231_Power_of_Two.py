# Leetcode 0231
# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0 or n == 1:
            return bool(n)
        if n % 2 == 1:
            return False

        return self.isPowerOfTwo(n // 2)