from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # O(1) Space
        n, m = len(matrix), len(matrix[0])
        col0 = 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0



        # O(n + m) Space Solution
        # rows = len(matrix)
        # cols = len(matrix[0])


        # rowSeen = [0] * rows
        # colSeen = [0] * cols

        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             rowSeen[i] = 1
        #             colSeen[j] = 1
        
        # for i in range(rows):
        #     for j in range(cols):
        #         if rowSeen[i] or colSeen[j]:
        #             matrix[i][j] = 0


        
        # Initial idea
        # rows = len(matrix)
        # cols = len(matrix[0])

        # seen = []

        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == 0:
        #             seen.append([i,j])
        
        # for i,j in seen:
        #     for k in range(cols):
        #         matrix[i][k] = 0
        #     for k in range(rows):
        #         matrix[k][j] = 0


        
