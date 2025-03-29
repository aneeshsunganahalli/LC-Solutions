from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures) # Start with zeros as some days don't have days with higher temp
        stack = [] # (index, temp) pairs

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]: # When stack isn't empty and the current temp is greater than top of stack temp, then we need to pop, because we reached a temp thats higher
                stackIndex, stackTemp = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((i,t)) # Adding pairs regardless if condition is met or not

        return res