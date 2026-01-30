# Minimum Window Subsequence

# You are given two strings, s1 and s2. Your task is to find the smallest substring in s1 such that s2 appears as a subsequence within that substring.

#     The characters of s2 must appear in the same sequence within the substring of s1.
#     If there are multiple valid substrings of the same minimum length, return the one that appears first in s1.
#     If no such substring exists, return an empty string.

# Note: Both the strings contain only lowercase english letters.

# Examples:

# Input: s1 = "geeksforgeeks", s2 = "eksrg"
# Output: "eksforg"
# Explanation: "eksforg" satisfies all required conditions. s2 is its subsequence and it is smallest and leftmost among all possible valid substrings of s1.

# Input: s1 = "abcdebdde", s2 = "bde" 
# Output: "bcde"
# Explanation:  "bcde" and "bdde" are two substring of s1 where s2 occurs as subsequence but "bcde" occur first so we return that.

class Solution:
    def minWindow(self, s1, s2):
        
        # Essentially the idea:
        #   - Satisfy (Look for a valid substring)
        #   - Minimize (Greedily shrink substring size till smallest possible)
        #   - Advance (Check for more substrings)
        
        i, j = 0, 0
        minlen = float('inf')
        res = [-1, -1]
        
        while i < len(s1):
            
            while i < len(s1) and j != len(s2):
                if s1[i] == s2[j]:
                    j += 1
                i += 1
                
            if j != len(s2):
                break
            
            tj = j - 1
            ti = i - 1
            
            while tj != -1:
                if s2[tj] == s1[ti]:
                    tj  -= 1
                ti -= 1
            
            if minlen > (i - 1) - ti:
                minlen = i - 1 - (ti)
                res = [ti + 1, i - 1]
            
            j = 0
            i = ti + 2
        
        l, r = res
        return s1[l: r + 1] if minlen != float('inf') else ""
        
        