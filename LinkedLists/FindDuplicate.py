from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]   # We need it iterate faster

            if slow == fast:
                break   # We can now introduce a second slow pointer starting from index 0
        
        slow2 = 0 
        # Slow2 and slow will be the same distance away from the start of the cycle from opposite ends, so when they meet we know we have reached our duplicate
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
            