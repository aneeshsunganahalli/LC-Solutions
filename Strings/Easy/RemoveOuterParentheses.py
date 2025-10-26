# 1021
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        res = ""
        balance = 0
        start = 0

        for i, c in enumerate(s):
            if c == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                res += s[start + 1: i]
                start = i + 1
        return res
