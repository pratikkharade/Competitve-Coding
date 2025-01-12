# Leetcode 0119
# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        output = [[1], [1, 1]]

        for i in range(2, rowIndex + 1):
            temp_list = []
            for j in range(i - 1):
                total = output[i - 1][j] + output[i - 1][j + 1]
                temp_list.append(total)
            output.append([1] + temp_list + [1])

        return output[rowIndex]

