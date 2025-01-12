# Leetcode 0022
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def dfs(self, open, close, s, res, n):
        if open == close and (open + close == 2 * n):
            res.append(s)
            return res

        if open < n:
            res = self.dfs(open + 1, close, s + "(", res, n)
        if close < open:
            res = self.dfs(open, close + 1, s + ")", res, n)
        return res

    def generateParenthesis(self, n: int) -> List[str]:
        return self.dfs(0, 0, "", [], n)