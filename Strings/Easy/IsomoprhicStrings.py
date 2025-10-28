# 205
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map1, map2 = [0] * 256, [0] * 256
        n = len(s)

        for i in range(n):
            if map1[ord(s[i])] != map2[ord(t[i])]:
                return False
            
            map1[ord(s[i])] = i + 1
            map2[ord(t[i])] = i + 1
        
        return True