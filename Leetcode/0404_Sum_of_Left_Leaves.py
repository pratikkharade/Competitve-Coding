# Leetcode 0404
# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, flag, sum):
        if flag and not node.left and not node.right:
            sum += node.val
        if node.left:
            sum = self.traverse(node.left, True, sum)
        if node.right:
            sum = self.traverse(node.right, False, sum)

        return sum

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.traverse(root, False, 0)