from typing import List
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = defaultdict(int)
        l = 0
        r = 0
        res = 0

        while r < len(s):
            if seen[s[r]] == 0:
                seen[s[r]] = 1
                res = max(res, r - l + 1)
                r += 1
            else:
                seen[s[l]] = 0
                l += 1
        return res