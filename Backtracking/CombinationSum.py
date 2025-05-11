from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, cur, total):
            if total == target:     # If we reach target, add subset
                res.append(cur.copy())  # Add copy, as cur will be modified
                return
            
            if i >= len(candidates) or total > target:  # Out of Bounds Conditions
                return 
            
            cur.append(candidates[i]) # Adding current number to subset
            dfs(i, cur, total + candidates[i])

            cur.pop() # Removing the number, to traverse path where we skip the number, we go to next index
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res