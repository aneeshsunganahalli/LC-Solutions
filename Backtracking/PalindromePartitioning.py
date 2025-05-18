from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        substr = []

        def backtrack(i):
            if i >= len(s):
                res.append(substr.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    substr.append(s[i : j+1])
                    backtrack(j + 1)
                    substr.pop()

        backtrack(0)
        return res
        
    def isPalindrome(self, s: str, l: int, r: int):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True