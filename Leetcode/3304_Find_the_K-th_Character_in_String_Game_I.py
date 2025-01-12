# Leetcode 3304
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution:
    def generate(self, word):
        for char in word:
            if ord(char) == 122:
                word += "a"
            else:
                word += chr(ord(char) + 1)
        return word

    def recursion(self, word, k):
        if k == 0:
            return word
        return self.recursion(self.generate(word), k//2)

    def kthCharacter(self, k: int) -> str:
        if k == 1:
            return "a"
        word = "a"
        word = self.recursion(word, k)
        return word[k-1]