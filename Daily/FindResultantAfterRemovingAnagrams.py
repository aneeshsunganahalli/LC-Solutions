from typing import List
# 2273
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        # Sorted solution
        result = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) == sorted(result[-1]):
                continue
            result.append(words[i])
        return result

        # Initial Solution, just as good
        def count(string):
            hm = {}
            for c in string:
                if c not in hm:
                    hm[c] = 1
                else:
                    hm[c] += 1
            return hm

        res = [words[0]]
        curr = count(words[0])

        for i in range(1, len(words)):
            check = count(words[i])
            if check != curr:
                curr = check
                res.append(words[i])
        return res
                          
        