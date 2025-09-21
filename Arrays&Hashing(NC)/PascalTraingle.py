from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Cleaner but same method
        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1]
            temp = [1] * (i + 1)
            for j in range(1, i):
                temp[j] = prev[j - 1] + prev[j]
            res.append(temp)
        return res

        # Initial Solution
        res = [[1], [1,1]]

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return res
        
        for i in range(3, numRows + 1):
            prev = res[-1]
            l, r = 0, i - 1
            temp = [0] * i
            temp[l], temp[r] = 1, 1
            j = 0
            while j + 1 < len(prev):
                l += 1
                temp[l] = prev[j] + prev[j + 1]
                j += 1
            res.append(temp)
        return res

