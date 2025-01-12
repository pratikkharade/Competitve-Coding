# Leetcode 0032
# https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = [-1]
        # substr = ""
        max_substr = 0
        for i in range(len(s)):
            print(l)
            if s[i] == '(':
                l.append(i)
            else:
                top = l.pop()
                if len(l):
                    max_substr = max(i - l[-1], max_substr)
                else:
                    l.append(i)

        return max_substr