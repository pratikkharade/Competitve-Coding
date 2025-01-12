# Leetcode 0094
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, inorder):
        if node.left:
            inorder = self.traverse(node.left, inorder)
        inorder.append(node.val)
        if node.right:
            inorder = self.traverse(node.right, inorder)
        return inorder

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.traverse(root, [])