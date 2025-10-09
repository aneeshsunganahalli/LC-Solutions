from typing import List
# 3494
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:

        m, n = len(mana), len(skill)
        prefix_skill = [0] * n

        for i in range(1, n):
            prefix_skill[i] = prefix_skill[i - 1] + skill[i]
        # prefix_skill[i] denotes total skill of wizards 0 to i
        
        potion_start_time = skill[0] * mana[0]
        for j in range(1, m):
            max_diff = skill[0] * mana[j]
            for i in range(1, n):
                """
                Bottleneck is caused by largest wait time, wait time is found after two conditions:
                    - current wizard should have finished the previous potion
                    - current potion should be brewed the previous wizard
                Obviously it takes longer for the current wizard to reach the current potion,
                that'i why the difference is calculated shown below
                """
                curr_diff = mana[j - 1] * prefix_skill[i] - mana[j] * prefix_skill[i - 1]
                if curr_diff > max_diff:
                    max_diff = curr_diff
            
            potion_start_time += max_diff
        # We have the start time of the last potion so we just add product of last potion and skill of all wizards.
        total = potion_start_time + mana[-1] * prefix_skill[-1]
        return total