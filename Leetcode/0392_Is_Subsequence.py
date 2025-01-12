# Leetcode 0392
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seq = t
        for i in range(len(s)):
            x = s[i]
            idx = seq.find(x)
            if idx == -1:
                return False
            seq = seq[idx+1:]
        return True

