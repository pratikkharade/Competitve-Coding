# Leetcode 2900
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]

        for i in range(1, len(words)):
            if groups[i - 1] != groups[i]:
                res.append(words[i])

        return res