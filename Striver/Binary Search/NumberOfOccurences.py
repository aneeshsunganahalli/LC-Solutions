"""
Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

Examples :

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
"""

class Solution:
    def countFreq(self, nums, target):
        
        def lowerBound(nums, low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1 
                else:
                    high =  mid - 1
            return low
        
        low = 0
        high = len(nums) - 1
        start = lowerBound(nums, low, high, target)
        end = lowerBound(nums, low, high, target + 1) - 1
        
        if start < len(nums) and nums[start] == target:
            return end - start + 1
        else:
            return 0
        