from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ''
        for s in strs:
            e += str(len(s)) + '#' + s
        return e


    def decode(self, s: str) -> List[str]:

        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res