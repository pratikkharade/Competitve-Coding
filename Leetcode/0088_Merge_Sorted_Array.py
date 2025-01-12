# Leetcode 0088
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        i = 0
        j = 0
        while m > 0 and n > 0:
            if nums1[i] <= nums2[j]:
                i += 1
                m -= 1
            else:
                nums1.pop()
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                n -= 1
        if n > 0:
            while n > 0:
                nums1.pop()
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                n -= 1
        if m > 0:
            while m > 0:
                i += 1
                m -= 1