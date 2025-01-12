# Leetcode 0104
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, depth, depths):
        if node.left:
            depths = self.traverse(node.left, depth + 1, depths)
        if node.right:
            depths = self.traverse(node.right, depth + 1, depths)
        if not node.left and not node.right:
            depths.append(depth)
        return depths

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        depth = 1
        if not root.left and not root.right:
            return depth

        depths = self.traverse(root, depth, [])
        return max(depths)