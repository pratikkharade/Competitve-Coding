# Leetcode 3364
# https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')

        for i in range(l, r + 1):
            x = 0
            total = sum(nums[:i])
            if total > 0:
                min_sum = min(total, min_sum)

            for x in range(1, len(nums) - i + 1):
                total = total - nums[x - 1] + nums[x + i - 1]
                if total > 0:
                    min_sum = min(total, min_sum)

        return min_sum if min_sum != float('inf') else -1