# Leetcode 0542
# https://leetcode.com/problems/01-matrix/description/

class Solution:
    # Dynamic Programming
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        dp = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    top = dp[i - 1][j] if i > 0 else float('inf')
                    left = dp[i][j - 1] if j > 0 else float('inf')
                    dp[i][j] = min(top, left) + 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    bottom = dp[i + 1][j] if i + 1 < m else float('inf')
                    right = dp[i][j + 1] if j + 1 < n else float('inf')
                    dp[i][j] = min(dp[i][j], min(bottom, right) + 1)

        return dp