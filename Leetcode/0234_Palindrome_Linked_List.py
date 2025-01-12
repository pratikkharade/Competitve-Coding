# Leetcode 0234
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursion(self, head, nodesList):
        if not head:
            return nodesList
        nodesList.append(head.val)
        return self.recursion(head.next, nodesList)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # RECURSIVE
        nodesList = self.recursion(head, [])
        print(nodesList)
        i = 0
        j = len(nodesList) - 1
        while i <= j:
            if nodesList[i] == nodesList[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

        # ITERATIVE
        # nodesList = []
        # while head:
        #     nodesList.append(head.val)
        #     head = head.next
        # i = 0
        # j = len(nodesList) - 1
        # while i <= j:
        #     if nodesList[i] == nodesList[j]:
        #         i += 1
        #         j -= 1
        #     else:
        #         return False
        # return True