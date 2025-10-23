// Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix.

// Examples:

// Input: mat[][] = [[1, 3, 5], 
//                 [2, 6, 9], 
//                 [3, 6, 9]]
// Output: 5
// Explanation: Sorting matrix elements gives us [1, 2, 3, 3, 5, 6, 6, 9, 9]. Hence, 5 is median.

// Input: mat[][] = [[2, 4, 9],
//                 [3, 6, 7],
//                 [4, 7, 10]]
// Output: 6
// Explanation: Sorting matrix elements gives us [2, 3, 4, 4, 6, 7, 7, 9, 10]. Hence, 6 is median.

// Input: mat = [[3], [4], [8]]
// Output: 4
// Explanation: Sorting matrix elements gives us [3, 4, 8]. Hence, 4 is median.

class Solution {
    public int median(int[][] mat) {
        
        int n = mat.length;
        int m = mat[0].length;
        
        int lo = mat[0][0];
        int hi = mat[0][m - 1];
        
        for(int i = 0; i < n; i++) {
            lo = Math.min(lo, mat[i][0]);
            hi = Math.max(hi, mat[i][m - 1]);
        }
        
        int total = m * n;
        int half = total / 2;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (count(mid, mat) <= half)
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        return lo;
        
    }
    
    public int count(int num, int[][] mat) {
        int c = 0;
        for (int i = 0; i < mat.length; i++) {
            int l = 0, r = mat[0].length - 1;
            while (l <= r) {
                int m = (l + r) / 2;
                if (mat[i][m] > num)
                    r = m - 1;
                else {
                    l = m + 1;
                }
            }
            c += l;
        }
        return c;
    }
}