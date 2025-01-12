# Leetcode 1572
# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)

        total = 0
        for i in range(m):
            total += mat[i][i]
        for i in range(m):
            total += mat[i][m-i-1]

        if m%2 == 1:
            mid = m//2
            total -= mat[mid][mid]
        return total