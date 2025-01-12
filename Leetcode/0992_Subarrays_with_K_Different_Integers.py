# Leetcode 0992
# https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if len(set(nums)) < k:
            return 0

        count = 0

        if len(set(nums)) == k:
            count += 1

        for i in range(k, len(nums)):
            sub_arr = nums[:i]
            if len(set(sub_arr)) == k:
                count += 1

            for j in range(1, len(nums) - i + 1):
                sub_arr.pop(0)
                sub_arr.append(nums[j + i - 1])
                if len(set(sub_arr)) == k:
                    count += 1

        return count