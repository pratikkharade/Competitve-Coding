# Leetcode 0637
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append([root])
        ans = []
        while q:
            nodes = q.popleft()
            total = 0
            temp_q = []
            for node in nodes:
                total += node.val
                if node.left:
                    temp_q.append(node.left)
                if node.right:
                    temp_q.append(node.right)
            if len(temp_q):
                q.append(temp_q)
            ans.append(total/len(nodes))
        return ans