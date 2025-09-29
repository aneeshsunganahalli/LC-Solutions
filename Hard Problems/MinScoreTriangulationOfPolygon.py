class Solution:
    def minScoreTriangulation(self, values) -> int:
        """
        According to the hint, since we can divide into subproblems A[1:k] and A[k + 1: n - 1],
        this follows the condition for the DP technique Matrix Chain Mulitplication, since we are 
        find min cost,

        You can divide matrices m1 m2 m3 m4, by taking first partition in n - 1 diff ways,
        basically to find min cost between m1 and m4 take the points in between as part of your 
        triangle and keep track of minimum cost in ur dp array

        Ex: m1 m2 m3 m4 m5 partitions look like
        (m1 m2)         (m3, m4, m5)
        (m1 m2 m3)      (m4 m5)
        (m1 m2 m3 m4)   (m5)
        """
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        
        # dp[i][j] = minimum score to triangulate the polygon between vertices i and j

        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                dp[i][j] = float('inf')

                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[0][n - 1] # This is where the min cost between the first and last vertices will be

