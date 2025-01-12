# Leetcode 0002
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        num1 = l1
        num2 = l2
        resHead = None
        currNode = None
        prevNode = None
        while num1 and num2:
            total = num1.val + num2.val + carry
            carry = total // 10
            total = total % 10
            currNode = ListNode(total)
            if resHead == None:
                resHead = currNode
            if prevNode:
                prevNode.next = currNode

            num1 = num1.next
            num2 = num2.next
            prevNode = currNode

        if num1:
            while num1:
                total = num1.val + carry
                carry = total // 10
                total = total % 10
                currNode = ListNode(total)
                if resHead == None:
                    resHead = currNode
                if prevNode:
                    prevNode.next = currNode

                num1 = num1.next
                prevNode = currNode

        if num2:
            while num2:
                total = num2.val + carry
                carry = total // 10
                total = total % 10
                currNode = ListNode(total)
                if resHead == None:
                    resHead = currNode
                if prevNode:
                    prevNode.next = currNode
                prevNode = currNode
                num2 = num2.next

        if carry == 1:
            currNode = ListNode(carry)
            if prevNode:
                prevNode.next = currNode
            prevNode = currNode
        return resHead