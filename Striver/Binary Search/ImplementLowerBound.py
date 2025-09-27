"""
Given a sorted array arr[] and a number target, the task is to find the lower bound of the target in this given array. The lower bound of a number is defined as the smallest index in the sorted array where the element is greater than or equal to the given number.

Note: If all the elements in the given array are smaller than the target, the lower bound will be the length of the array. 
"""

class Solution:
    def lowerBound(self, arr, target):
        
        
        low = 0
        high = len(arr) - 1
        res = len(arr)
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] >= target:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res