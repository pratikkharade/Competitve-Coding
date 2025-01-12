# Leetcode
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        parenthesisList = []
        if len(s) == 1:
            return False
        for i in s:
            if i == '(' or i == '{' or i == '[':
                parenthesisList.append(i)
            else:
                if len(parenthesisList) == 0:
                    return False
                top = parenthesisList.pop()
                if (top == '(' and i == ')') or (top == '[' and i == ']') or (top == '{' and i == '}'):
                    continue
                else:
                    return False
        if len(parenthesisList) == 0:
            return True
        else:
            return False

