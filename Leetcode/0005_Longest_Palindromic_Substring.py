# Leetcode 0005
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        x = 0
        y = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                x = i
                y = i + 1

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    x = i
                    y = j

        return s[x: y + 1]