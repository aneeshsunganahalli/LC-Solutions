# 76
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l = 0
        tc, curr = Counter(t), {}
        unique = len(tc)
        req = 0
        res, minLen = [-1,-1], float('inf')

        for r, ch in enumerate(s):
            curr[ch] = curr.get(ch, 0) + 1

            if ch in tc and tc[ch] == curr[ch]:
                req += 1
        
                while l <= r and req == unique:

                    if minLen > r - l + 1:
                        minLen = r - l + 1
                        res = [l, r]

                    curr[s[l]] -= 1
                    if s[l] in tc and curr[s[l]] < tc[s[l]]:
                        req -= 1
                    l += 1
        l, r = res
        return s[l: r + 1] if minLen != float('inf') else ""



