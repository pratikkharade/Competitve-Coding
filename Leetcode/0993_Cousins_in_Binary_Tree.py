# Leetcode 0993
# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, None)])

        while len(q):
            result = []
            for i in range(len(q)):
                node, parent = q.popleft()
                if node.val == x:
                    if parent:
                        result.append(parent)
                if node.val == y:
                    if parent:
                        result.append(parent)
                if node.left:
                    q.append([node.left, node.val])
                if node.right:
                    q.append([node.right, node.val])

            if len(set(result)) == 2:
                return True
        return False