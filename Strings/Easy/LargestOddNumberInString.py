# 1903
class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        n = len(num)
        last = n - 1
        flag = False
        for c in range(n - 1, -1, -1):
            if int(num[c]) % 2:
                flag = True
                last = c
                break
        return num[:last + 1] if flag else ""
        