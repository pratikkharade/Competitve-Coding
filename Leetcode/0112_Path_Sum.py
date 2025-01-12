# Leetcode 0112
# https://leetcode.com/problems/path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, node, sums, sum):
        if node.left:
            sums = self.pathSum(node.left, sums, sum + node.left.val)
        if node.right:
            sums = self.pathSum(node.right, sums, sum + node.right.val)
        if not node.left and not node.right:
            sums.append(sum)
        return sums

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        sums = self.pathSum(root, [], root.val)

        return targetSum in sums