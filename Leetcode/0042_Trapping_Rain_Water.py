# Leetcode 0042
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        # SOLUTION 1
        i, j = 0, len(height) - 1
        left_max, right_max = 0, 0
        total = 0

        while i <= j:
            if height[i] <= height[j]:
                if height[i] >= left_max:
                    left_max = height[i]
                else:
                    total += left_max - height[i]
                i += 1
            else:
                if height[j] >= right_max:
                    right_max = height[j]
                else:
                    total += right_max - height[j]
                j -= 1
        return total

        # SOLUTION 2
        # res = [-1] * len(height)
        # res[0] = 0
        # res[len(res) - 1] = 0

        # max_left = [-1] * len(height)
        # max_left[0] = height[0]
        # for i in range(1, len(height)):
        #     max_left[i] = max(height[i], max_left[i-1])

        # max_right = [-1] * len(height)
        # max_right[len(max_right)-1] = height[len(height)-1]
        # for i in range(len(max_right)-2, -1, -1):
        #     max_right[i] = max(height[i], max_right[i+1])

        # for i in range(1, len(height) - 1):
        #     res[i] = min(max_left[i], max_right[i]) - height[i]

        # return sum(res)