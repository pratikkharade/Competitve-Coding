# Leetcode 0118
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        output = [[1], [1, 1]]

        for i in range(2, numRows):
            temp_list = []
            for j in range(i - 1):
                temp_list.append(output[i - 1][j] + output[i - 1][j + 1])
            output.append([1] + temp_list + [1])

        return output