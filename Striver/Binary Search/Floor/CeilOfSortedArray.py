"""
Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x. This element is called the floor of x. If such an element does not exist, return -1.
"""
class Solution:
    def findFloor(self, nums, x):
        
        
        low = 0
        high = len(nums) - 1
        res = - 1
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
    
"""
Given a sorted array arr[] and an integer x, find the index (0-based) of the smallest element in arr[] that is greater than or equal to x. This element is called the ceil of x. If such an element does not exist, return -1.
"""
class Solution:
    def findCeil(self, nums, x):
        
        
        low = 0
        high = len(nums) - 1
        res = - 1
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] < x:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res
    
  