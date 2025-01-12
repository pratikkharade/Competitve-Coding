# Leetcode 0021
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursion(self, list1, list2, mergedList):
        if list1 and list2:
            if list1.val < list2.val:
                mergedList.append(list1.val)
                mergedList = self.recursion(list1.next, list2, mergedList)
            else:
                mergedList.append(list2.val)
                mergedList = self.recursion(list1, list2.next, mergedList)
        elif list1 and not list2:
            mergedList.append(list1.val)
            mergedList = self.recursion(list1.next, list2, mergedList)
        elif not list1 and list2:
            mergedList.append(list2.val)
            mergedList = self.recursion(list1, list2.next, mergedList)

        return mergedList

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        mergedList = self.recursion(list1, list2, [])

        if not mergedList:
            return None

        nextNode = None
        for val in mergedList[::-1]:
            node = ListNode(val, nextNode)
            nextNode = node
        return node