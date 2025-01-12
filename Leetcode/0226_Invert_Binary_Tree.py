# Leetcode 0226
# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, node):
        temp_left, temp_right = None, None
        if node.left:
            temp_left = node.left
        if node.right:
            temp_right = node.right

        if temp_left and temp_right:
            node.left = node.right
            node.right = temp_left
        elif node.left and not node.right:
            node.right = node.left
            node.left = None
        elif not node.left and node.right:
            node.left = node.right
            node.right = None

        if node.left:
            self.invert(node.left)
        if node.right:
            self.invert(node.right)
        return

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.invert(root)
        return root