# Leetcode 1328
# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, pal: str) -> str:
        n = len(pal)

        if n == 1:
            return ""
        for i in range(n//2):
            if pal[i] != 'a':
                return pal[:i] + 'a' + pal[i+1:]
        return pal[:n-1] + 'b'