from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Used to init a dict without actual key values

        for s in strs:
            count = [0]*26

            for i in s:
                count[ord(i) - ord('a')] += 1
            res[tuple(count)].append(s) # Have to use tuple, can't use array as key for dict
        return list(res.values())