# Leetcode 0013
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        if len(s) == 1:
            return map[s[0]]

        num = 0
        i = 0

        while i < len(s) - 1:
            if map[s[i]] >= map[s[i + 1]]:
                num += map[s[i]]
                if i == len(s) - 2:
                    num += map[s[i + 1]]
                i += 1
            else:
                num += map[s[i + 1]] - map[s[i]]
                i += 2
                if i == len(s) - 1:
                    num += map[s[i]]
        return num