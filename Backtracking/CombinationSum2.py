from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()  # Sorting to keep duplicates adjacent

        def dfs(i, cur, total):
            # Base Cases
            if target == total:
                res.append(cur.copy())
                return
            
            if i == len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])

            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:   # Skipping duplicates
                i += 1
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res





class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Easier Solution
        res = set()
        candidates.sort()   # Sorting to keep duplicates adjacent

        def dfs(i, cur, total):
            # Base Cases
            if total == target:
                res.add(tuple(cur))
                return
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i]) # Choosing the current index
            dfs(i + 1, cur, total + candidates[i])

            cur.pop()   # Skipping the current number
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return [list(combination) for combination in res] # List Comphrenshion to convert set into list