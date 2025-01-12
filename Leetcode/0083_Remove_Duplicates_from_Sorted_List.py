# Leetcode 0083
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        ptr1 = head
        ptr2 = head.next
        while ptr2:
            if ptr1.val == ptr2.val:
                ptr1.next = None
                ptr2 = ptr2.next
            else:
                ptr1.next = ptr2
                ptr1 = ptr2
                ptr2 = ptr2.next
        return head