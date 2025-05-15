from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        res = []
        numberHash = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, cur):
            if i >= len(digits):
                res.append(cur)
                return
            for ch in numberHash[digits[i]]:
                backtrack(i + 1, cur + ch)

        backtrack(0, '')
        return res