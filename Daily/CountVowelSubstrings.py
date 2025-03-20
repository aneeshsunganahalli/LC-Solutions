class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        # Not most optimal but works okay
        v = {'a','e','i','u','o'}
        c = 0

        for i in range(len(word)-4):
            for j in range(i+5,len(word) + 1):
                if set(word[i:j]) == v:
                    c += 1
        return c