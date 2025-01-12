# Leetcode 0102
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        q = deque()
        visited = []
        q.append([root])

        while len(q) > 0:
            nodes = q.popleft()
            temp_q = []
            temp_visited = []
            for node in nodes:
                temp_visited.append(node.val)
                if node.left:
                    temp_q.append(node.left)
                if node.right:
                    temp_q.append(node.right)
            if len(temp_q):
                q.append(temp_q)
            visited.append(temp_visited)
        return visited