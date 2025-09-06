class Solution:
    def longestSubarray(self, nums, k):  
        
        n = len(nums)
        hashmap = {}
        maxlen = 0
        prefixSum = 0
        
        for i in range(n):
            prefixSum += nums[i]
            
            if prefixSum == k:
                maxlen = max(maxlen, i + 1)
            if prefixSum - k in hashmap:
                maxlen = max(maxlen, i - hashmap[prefixSum - k])
            if prefixSum not in hashmap:
                hashmap[prefixSum] = i
        
        return maxlen