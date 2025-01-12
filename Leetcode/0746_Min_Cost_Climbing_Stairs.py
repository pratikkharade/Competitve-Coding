# Leetcode 0746
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        sum = [0] * n
        sum[0] = cost[0]
        sum[1] = cost[1]

        for i in range(2, n):
            sum[i] = min(sum[i - 1], sum[i - 2]) + cost[i]

        return min(sum[n - 1], sum[n - 2])