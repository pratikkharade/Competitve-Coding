# Leetcode 0145
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, preorder):
        if node.left:
            preorder = self.traverse(node.left, preorder)
        if node.right:
            preorder = self.traverse(node.right, preorder)

        preorder.append(node.val)
        return preorder

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.traverse(root, [])