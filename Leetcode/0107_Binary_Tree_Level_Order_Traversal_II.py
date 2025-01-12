# Leetcode 0107
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        v = []
        q = deque()
        q.append([root])

        while len(q):
            nodes = q.popleft()
            temp_q = []
            temp_v = []
            for node in nodes:
                temp_v.append(node.val)
                if node.left:
                    temp_q.append(node.left)
                if node.right:
                    temp_q.append(node.right)
            if len(temp_q):
                q.append(temp_q)
            v.append(temp_v)
        return v[::-1]
