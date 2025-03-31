class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Optimal Sliding Window
        if len(s1) > len(s2):
            return False        # No permutation possible
        
        s1Map, s2Map = [0]*26, [0]*26  # Maps used to store freq of all 26 letters in s1 and s2
        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1
            s2Map[ord(s2[i]) - ord('a')] += 1
        
        matches  = 0
        for i in range(26):
            matches += (1 if s1Map[i] == s2Map[i] else 0) # Checks out how many of 26 letters freq match
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True  # All character frequencies match so perm possible
            
            index = ord(s2[r]) - ord('a')
            s2Map[index] += 1
            if s1Map[index] == s2Map[index]:
                matches += 1    # Extra match found
            elif s1Map[index] + 1 == s2Map[index]:
                matches -= 1    # A match lost
            
            leftIndex = ord(s2[l]) - ord('a')
            s2Map[leftIndex] -= 1
            if s2Map[leftIndex] == s1Map[leftIndex]:
                matches += 1
            elif s1Map[leftIndex] - 1 == s2Map[leftIndex]:
                matches -= 1
            l +=1 
        return matches == 26