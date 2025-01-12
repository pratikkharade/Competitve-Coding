# Leetcode 661
# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        res = []

        for i in range(m):
            temp = []
            for j in range(n):
                adj = []
                adj.append(img[i][j])
                if i > 0:
                    adj.append(img[i - 1][j])
                if j > 0:
                    adj.append(img[i][j - 1])
                if i > 0 and j > 0:
                    adj.append(img[i - 1][j - 1])

                if i < m - 1:
                    adj.append(img[i + 1][j])
                if j < n - 1:
                    adj.append(img[i][j + 1])
                if i < m - 1 and j < n - 1:
                    adj.append(img[i + 1][j + 1])

                if i > 0 and j < n - 1:
                    adj.append(img[i - 1][j + 1])
                if j > 0 and i < m - 1:
                    adj.append(img[i + 1][j - 1])
                temp.append(floor(sum(adj) / len(adj)))
            res.append(temp)
        return res