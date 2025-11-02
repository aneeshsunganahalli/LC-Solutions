# 1781
class Solution:
    def beautySum(self, s: str) -> int:

        res = 0
        for i in range(len(s)):
            count = defaultdict(int)
            for j in range(i, len(s)):
                count[s[j]] += 1
                res += max(count.values()) - min(count.values())
        return res