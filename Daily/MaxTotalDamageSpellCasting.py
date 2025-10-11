# 3186
from collections import Counter
from typing import List
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        freq = Counter(power)
        sorted_keys = sorted(freq.keys())
        n = len(sorted_keys)
        dp = [0] * n

        for i in range(n):
            damage = freq[sorted_keys[i]] * sorted_keys[i]

            # index = bisect_right(sorted_keys, sorted_keys[i] - 3) - 1
            index = i - 1
            while index >= 0 and sorted_keys[index] >= sorted_keys[i] - 2:
                index -= 1

            dp[i] = max(dp[i - 1] if i > 0 else 0, damage + dp[index])
        return dp[-1]

        