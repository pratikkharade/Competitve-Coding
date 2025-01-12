# Leetcode 1721
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0

        temp = head
        vals = []
        while temp:
            n += 1
            temp = temp.next

        i = k - 1
        j = n - k

        if i == j:
            return head

        node = head
        for x in range(n):
            if x == i:
                node1 = node
            elif x == j:
                node2 = node
            node = node.next

        val = node1.val
        node1.val = node2.val
        node2.val = val

        return head