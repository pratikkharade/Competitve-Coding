# Leetcode 0058
# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()[::-1]
        index = s.find(" ")
        if index == -1:
            return len(s)
        else:
            return index