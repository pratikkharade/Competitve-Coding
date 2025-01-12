# Leetcode 0653
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, k, dict):
        if node.val in dict:
            return True
        else:
            dict[k - node.val] = dict.get(k - node.val, 0) + 1

        if node.left:
            dict = self.traverse(node.left, k, dict)
        if dict == True:
            return True

        if node.right:
            dict = self.traverse(node.right, k, dict)
        if dict == True:
            return True
        else:
            return dict

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root or (not root.left and not root.right):
            return False

        dict = self.traverse(root, k, {})
        if dict == True:
            return True
        else:
            return False