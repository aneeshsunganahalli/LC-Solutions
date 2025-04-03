class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}     # Maps to store frequencies

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        have, need = 0, len(countT)
        
        res, resLen = [-1,-1], float('inf')     # Used to store boundary of valid substring and the length
        l = 0
        for r in range(len(s)):
            c = s[r]    # Obtaining the character
            window[c] = 1 + window.get(c, 0) # Adding freq into the window hashmap

            if c in countT and window[c] == countT[c]:
                have += 1   # We have one of the characters we need
            
            while have == need:
                if (r - l + 1) < resLen:    # Updates min length and indices
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1 # No longer have enough of a character
                l += 1
        l, r = res
        print(res)
        return s[l: r + 1] if resLen != float('inf') else ""