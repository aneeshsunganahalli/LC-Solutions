from collections import defaultdict

class Solution: # Slightly Faster Solution
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        last = [-1,-1,-1]
        for i in range(N):
            last[ord(s[i]) - ord('a')] = i
            res = res + 1 + min(last[0],min(last[1],last[2]))

        return res

class Solution: # My own solution
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        l = 0
        count = defaultdict(int)       

        for r in range(N):
            count[s[r]] += 1
            
            while len(count) == 3:
                res += N - r

                count[s[l]] -= 1

                if count[s[l]] == 0:
                    count.pop(s[l])
                l += 1
        return res
