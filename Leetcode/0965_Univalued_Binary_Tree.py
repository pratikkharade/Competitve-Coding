# Leetcode 0965
# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, target):
        if node.val != target:
            return False
        if node.left:
            if not self.traverse(node.left, target):
                return False

        if node.right:
            if not self.traverse(node.right, target):
                return False

        return True

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True

        return self.traverse(root, root.val)