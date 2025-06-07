class Solution:
    def climbStairs(self, n: int) -> int:

        # Tabulation
        if n < 2:
            return n
            
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

        # Memoization
        cache = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)
        
        # Regular Recursion
        def dfs(i):
            if i >= n:
                return i == n # Returns 0 for False and 1 for True
            return dfs(i + 1) + dfs(i + 2)  # Adds all possible paths
        return dfs(0)