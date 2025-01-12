# Leetcode 0206
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursion(self, prev, curr, temp):
        if not curr:
            return prev

        curr.next = prev
        prev = curr
        curr = temp
        if temp:
            temp = temp.next

        return self.recursion(prev, curr, temp)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # RECURSIVE
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        temp = head.next.next

        prev.next = None
        return self.recursion(prev, curr, temp)

        # ITERATIVE
        # if not head or not head.next:
        #     return head

        # prev = head
        # curr = head.next
        # temp = head.next.next

        # prev.next = None
        # while curr:
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        #     if temp:
        #         temp = temp.next

        # return prev