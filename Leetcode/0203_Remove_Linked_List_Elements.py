# Leetcode 203
# https://leetcode.com/problems/remove-linked-list-elements/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursion(self, head, node, prev, val):
        if not node:
            return head

        if node.val == val:
            if node == head:
                node = node.next
                head = node
                head = self.recursion(head, node, prev, val)
            else:
                node = node.next
                prev.next = node
                head = self.recursion(head, node, prev, val)
        else:
            prev = node
            node = node.next
            head = self.recursion(head, node, prev, val)

        return head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        # RECURSIVE
        return self.recursion(head, head, None, val)

        # ITERATIVE
        # prev = None
        # curr = head

        # while curr:
        #     if curr.val == val:
        #         if curr == head:
        #             curr = curr.next
        #             head = curr
        #         else:
        #             curr = curr.next
        #             prev.next = curr
        #     else:
        #         prev = curr
        #         curr = curr.next
        # return head