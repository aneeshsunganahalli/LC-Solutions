from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        N = len(questions)
        cache = [0] * N     # To store values we've seen before

        def backtrack(i):
            if i >= N:
                return 0    # Out of Bounds
            
            if cache[i]:    # If value is non-zero,
                return cache[i]
            
            points, brainpower = questions[i]
            
            cache[i] = max(
                backtrack(i+1),     # Skipping current question
                points + backtrack(i + 1 + brainpower)  # Answering current question
            )

            return cache[i]
        
        return backtrack(0)