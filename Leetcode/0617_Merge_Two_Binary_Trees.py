# Leetcode 0617
# https://leetcode.com/problems/merge-two-binary-trees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, node1, node2):
        if node1 and node2:
            node = TreeNode(node1.val + node2.val)

        if node1.left and node2.left:
            node.left = self.merge(node1.left, node2.left)
        elif node1.left and not node2.left:
            node.left = node1.left
        elif not node1.left and node2.left:
            node.left = node2.left

        if node1.right and node2.right:
            node.right = self.merge(node1.right, node2.right)
        elif node1.right and not node2.right:
            node.right = node1.right
        elif not node1.right and node2.right:
            node.right = node2.right

        return node

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        return self.merge(root1, root2)