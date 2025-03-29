from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(p,s) for p,s in zip(position,speed)] # Build Array of speed and pos pairs
        cars.sort(reverse=True) # Sort in reverse order, we check highest pos first
        stack = []

        for p,s in cars:
            stack.append((target - p)/ s) # Append the time of current car
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # If second top most is greater than top most
                            # then they become part of same fleet, as the behind car has caught up
        return len(stack) # All the times that aren't in same fleet will be left in stack, so return length to get number of fleets