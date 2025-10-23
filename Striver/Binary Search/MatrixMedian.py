"""
Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix.

Examples:

Input: mat[][] = [[1, 3, 5], 
                [2, 6, 9], 
                [3, 6, 9]]
Output: 5
Explanation: Sorting matrix elements gives us [1, 2, 3, 3, 5, 6, 6, 9, 9]. Hence, 5 is median.

Input: mat[][] = [[2, 4, 9],
                [3, 6, 7],
                [4, 7, 10]]
Output: 6
Explanation: Sorting matrix elements gives us [2, 3, 4, 4, 6, 7, 7, 9, 10]. Hence, 6 is median.

Input: mat = [[3], [4], [8]]
Output: 4
Explanation: Sorting matrix elements gives us [3, 4, 8]. Hence, 4 is median.
"""
class Solution:
    def median(self, mat):
        
        n = len(mat)
        m = len(mat[0])
        
        minVal = mat[0][0]
        maxVal = mat[0][m - 1]
        
        for i in range(1,n):
            if minVal > mat[i][0]:
                minVal = mat[i][0]
                
            if maxVal < mat[i][m - 1]:
                maxVal = mat[i][m - 1]
        
        def count(num):
            c = 0
            for row in mat:
                l,r = 0, len(row) - 1
                while l <= r:
                    m = (l + r) // 2
                    if row[m] > num:
                        r = m - 1
                    else:
                        l = m + 1
                c += l
            return c
                        
                
        
        lo = minVal
        hi = maxVal
        total = m * n
        half = total // 2
        res = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if count(mid) > half:
                hi = mid - 1
            else:
                res = mid
                lo = mid + 1
        return lo
                
        
    	