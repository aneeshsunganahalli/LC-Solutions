# 282
from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        n = len(num)
        res = []
        expr = []

        def helper(op: str, curr, last, sub):
            if op == "+":
                new_curr = curr + sub
                new_last = sub
            elif op == "-":
                new_curr = curr - sub
                new_last = -sub
            else:
                new_curr = curr - last + last * sub
                new_last = last * sub
            
            return new_curr, new_last


        def dfs(i, curr, last):
            if i == n:
                if curr == target:
                    e = expr.copy()
                    res.append("".join(e))
                return
            
            for j in range(i, n):
                if num[i] == "0" and j > i: # Hard constraint on leading zeros
                    break  

                sub = num[i: j + 1]
                s = int(sub)

                if i == 0:
                    expr.append(sub)
                    dfs(j + 1, s, s)
                    expr.pop()
                else:
                    for op in ("+", "-", "*"):
                        expr.append(op)
                        expr.append(sub)
                        new_curr, new_last = helper(op, curr, last, s)
                        dfs(j + 1, new_curr, new_last)
                        expr.pop()
                        expr.pop()
            
        dfs(0, 0, 0)
        return res
