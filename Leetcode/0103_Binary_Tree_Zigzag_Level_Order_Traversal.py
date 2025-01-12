# Leetcode 0103
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        q = deque()
        visited = []
        q.append([root])

        i = 0
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
            if i % 2 == 1:
                visited.append(temp_v[::-1])
            else:
                visited.append(temp_v)
            i += 1
        return visited