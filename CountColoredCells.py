class Solution:
    def coloredCells(self, n: int) -> int:

        # Mid Layer
        mid = 2*n - 1
        # Number of terms for the A.P Sum
        m = n - 1
        # Sum of A.P
        s = m/2 * (2*m)

        return int(mid + 2*s)
        