"""
Given an array arr[] containing both positive and negative integers, the task is to find the length of the longest subarray with a sum equals to 0.

Note: A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.
"""

class Solution:
    def maxLength(self, nums):
        
        
        seen = {}
        maxlen = 0
        prefixSum = 0
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            
            if prefixSum == 0:
                maxlen = max(maxlen, i + 1)
            
            elif prefixSum in seen:
                maxlen = max(maxlen, i - seen[prefixSum])
            else:
                seen[prefixSum] = i
        
        return maxlen
                