# Leetcode 0110
# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node):
        if node == None:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        lDepth = self.depth(root.left)
        rDepth = self.depth(root.right)
        if abs(lDepth - rDepth) < 2 and self.isBalanced(root.left) == True and self.isBalanced(root.right) == True:
            return True
        return False