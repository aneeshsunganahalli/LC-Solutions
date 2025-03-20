class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        i,j = 0,0
        res = 0


        while j < len(s):
            if seen[s[j]] == 0:
                seen[s[j]] = 1
                res = max(res, j - i + 1)
                j += 1
            else:
                seen[s[i]] = 0
                i += 1
        return res