from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        canCook = {s:True for s in supplies}    # Hash Map to store recipes that can be cooked, supplies are available so they can technically be cooked, recipe -> True/False
        recipe_index = {r:i for i,r in enumerate(recipes)} # Hash Map to get the index of a recipe, key -> value is recipe -> index

        def dfs(r):  # Main DFS function
            if r in canCook:
                return canCook[r]  # Return whether we know if it can be cooked or not
            
            if r not in recipe_index: # If r isn't in canCook it's not a supply and if its not in recipes either, then we can't cook
                return False
            
            canCook[r] = False # If two recipes depend on each other neither can be cooked, so we intialise to false
            
            for nei in ingredients[recipe_index[r]]: # We check neighbours of r and apply dfs
                if not dfs(nei): # If neighbour ingredients not available, then can't cook
                    return False

            canCook[r] = True # If all checked, then we can cook
            return canCook[r]
        
        
        res = []
        for r in recipes:
            if dfs(r):
                res.append(r) # Append all recipes that can be cooked
        return res