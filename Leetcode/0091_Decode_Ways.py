# Leetcode 0091
# https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        num = 0
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_digits = int(s[i - 1])
            two_digits = int(s[i - 2:i])
            print(one_digits, two_digits)

            if one_digits != 0:
                dp[i] = dp[i - 1]
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]
            print(dp)
        return dp[n]