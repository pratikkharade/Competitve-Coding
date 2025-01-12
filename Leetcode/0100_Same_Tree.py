# Leetcode 0100
# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (not p and q) or (p and not q):
            return False
        elif not p and not q:
            return True

        if p.val != q.val:
            return False

        if p.left and q.left:
            if not self.isSameTree(p.left, q.left):
                return False
        elif (p.left and not q.left) or (not p.left and q.left):
            return False

        if p.right and q.right:
            if not self.isSameTree(p.right, q.right):
                return False
        elif (p.right and not q.right) or (not p.right and q.right):
            return False

        return True