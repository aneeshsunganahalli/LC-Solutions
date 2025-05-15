from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        # Recursive Solution
        res = []
        self.helper(0, -1, words, groups, res)
        return res
        
    def helper(self, i: int, prev: int, words, groups, res):

        if i == len(words):
            return
        
        if groups[i] != prev:
            res.append(words[i])
        self.helper(i + 1, groups[i], words, groups, res)

        # Greedy Solution
        if not words or not groups:
            return []
        
        res = [words[0]]
        prev = groups[0]

        for i in range(1,len(words)):
            if groups[i] != prev:
                res.append(words[i])
                prev = groups[i]
        return res
