# Leetcode 0024
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursion(self, node1, node2, prev_node):
        node1.next = node2.next
        node2.next = node1
        if prev_node:
            prev_node.next = node2

        prev_node = node1
        node1 = node1.next
        if not node1:
            return
        node2 = node1.next
        if not node2:
            return
        return self.recursion(node1, node2, prev_node)

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node1 = head
        node2 = head.next

        node1.next = None
        self.recursion(node1, node2, None)
        return node2