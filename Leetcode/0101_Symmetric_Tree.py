# Leetcode 0101
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, node1, node2):
        if node1.val != node2.val:
            return False

        if node1.left and node2.right:
            if not self.compare(node1.left, node2.right):
                return False
        elif (node1.left and not node2.right) or (not node1.left and node2.right):
            return False

        if node1.right and node2.left:
            if not self.compare(node1.right, node2.left):
                return False
        elif (node1.right and not node2.left) or (not node1.right and node2.left):
            return False

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.left and root.right:
            return self.compare(root.left, root.right)
        elif (root.left and not root.right) or (not root.left and root.right):
            return False
        else:
            return True