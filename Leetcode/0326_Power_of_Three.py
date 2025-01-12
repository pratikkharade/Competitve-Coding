# Leetcode 0326
# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 or n == 1:
            return bool(n)
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n // 3)