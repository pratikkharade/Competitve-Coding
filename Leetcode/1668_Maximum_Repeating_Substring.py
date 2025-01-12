# Leetcode 1668
# https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        max_count = 0
        temp_word = word

        while temp_word in sequence:
            count += 1
            temp_word += word
            max_count = max(max_count, count)

        return max_count