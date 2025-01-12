# Leetcode 0035
# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def binarySearch(self, nums, start, end, target):
        mid = (start + end) // 2

        if start == end:
            return start

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return self.binarySearch(nums, start, mid, target)
        else:
            return self.binarySearch(nums, mid + 1, end, target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums), target)