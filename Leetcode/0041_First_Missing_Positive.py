# Leetcode 0041
# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [x for x in nums if x > 0]
        if len(nums) == 0:
            return 1

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if idx < len(nums) and nums[idx] > 0:
                nums[idx] = -1 * nums[idx]

        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1