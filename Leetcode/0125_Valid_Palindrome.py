# Leetcode 0125
# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        og = ""
        rev = ""
        for i in range(len(s)-1, -1, -1):
            if ((ord(s[i]) >= 48 and ord(s[i]) <= 57) or (ord(s[i]) >= 97 and ord(s[i]) <= 122)):
                og = og + s[i]
                rev = s[i] + rev
        return og == rev