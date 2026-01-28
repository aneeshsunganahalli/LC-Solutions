# Longest Substring with K Uniques

# You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

# Note : If no such substring exists, return -1. 

# Examples:

# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

# Input: s = "aaaa", k = 2
# Output: -1
# Explanation: There's no substring with 2 distinct characters.

from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        
        
        count = {}
        res = -1
        l = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
    
            if len(count) > k:
                res = max(res, r - l)
                
            while l < r and len(count) > k:
                count[s[l]] -= 1
                
                if count[s[l]] == 0:
                    del count[s[l]]
                    
                l += 1
                    
        if len(count) == k:
            res = max(res, r - l + 1)
            
        return res
        
        