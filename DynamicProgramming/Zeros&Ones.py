# 474
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # Basically a 2D Knapsack
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zero = s.count('0')
            one = s.count('1')

            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)
        return dp[m][n]

        # Memoised Solution
        dp = {}
        def dfs(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]
            
            m_count, n_count = strs[i].count('0'), strs[i].count('1')

            dont_pick = dfs(i + 1, m, n)
            pick = 0
            if m - m_count >= 0 and n - n_count >= 0:
                pick = 1 + dfs(i + 1, m - m_count, n - n_count)

            dp[(i, m, n)] = max(dont_pick, pick)
            return dp[(i ,m ,n)]
        
        return dfs(0, m, n)

        # TLE, regular recursion
        count = [(s.count('0'), s.count('1')) for s in strs]
        def dfs(i, m, n):
            if i == len(strs):
                return 0
            m_count, n_count = count[i]
            
            dont_pick = dfs(i + 1, m, n)
            pick = 0
            if m - m_count >= 0 and n - n_count >= 0:
                pick = 1 + dfs(i + 1, m - m_count, n - n_count)

            return max(dont_pick, pick)
        
        return dfs(0, m, n)
            

            
            
            
