# Leetcode 0509
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        # RECURSIVE
        if n < 2:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

        # ITERATIVE
        # if n < 2:
        #     return n
        # F = [-1]*(n+1)
        # F[0] = 0
        # F[1] = 1

        # for i in range(2, n+1):
        #     F[i] = F[i-1] + F[i-2]
        # return F[n]