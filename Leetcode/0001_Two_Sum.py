# Leetcode 0001
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return i, nums[i+1:].index(diff)+i+1