# Leetcode 0108
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createTree(self, nodes):
        if len(nodes) == 1:
            return nodes[0]
        elif len(nodes) == 2:
            nodes[1].left = nodes[0]
            return nodes[1]
        elif len(nodes) == 3:
            nodes[1].left = nodes[0]
            nodes[1].right = nodes[2]
            return nodes[1]
        mid = len(nodes)//2
        nodes[mid].left = self.createTree(nodes[:mid])
        nodes[mid].right = self.createTree(nodes[mid+1:])
        return nodes[mid]

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nodes = [TreeNode(nums[i]) for i in range(len(nums))]
        return self.createTree(nodes)