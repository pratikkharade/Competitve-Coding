# Leetcode 0067
# https://leetcode.com/problems/add-binary/

class Solution:
    def binToDec(self, x):
        num = 0
        for i in range(len(x)):
            num += int(x[i]) * pow(2, len(x) - i - 1)

        return num

    def decToBin(self, x):
        bin = ""
        if x == 0:
            return "0"
        while x >= 1:
            bin = str(int(x % 2)) + bin
            x = x // 2
        return bin

    def addBinary(self, a: str, b: str) -> str:
        x = self.binToDec(a)
        y = self.binToDec(b)
        res = x + y
        return self.decToBin(res)