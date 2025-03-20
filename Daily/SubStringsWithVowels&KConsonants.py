from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atleastK(k: int) -> int:
            vowels = defaultdict(int) # Hash for storing current vowel counts
            l = 0
            consonants = 0
            res = 0

            for r in range(len(word)):

                # Checking if current letter is vowel
                if word[r] in 'aeiou':
                    vowels[word[r]] += 1
                else:
                    consonants += 1
                
                # Shrinking Valid Substring to check it remains valid
                while len(vowels) == 5 and consonants >= k: # 1st Condition: Checks if all vowels present atleast once
                    res += len(word) - r                    # 2nd Condition Checks if we atleast k consonants
                    
                    if word[l] in 'aeiou':                  # Before shrinking window, checking letter at l pointer
                        vowels[word[l]] -= 1                # to see which type of letter is going to be removed.
                    else:
                        consonants -= 1

                    if vowels[word[l]] == 0:                # If l pointed to vowel and now that vowel's count == 0, 
                        vowels.pop(word[l])                 # then remove it from vowels hash, to break while loop condition
                    l += 1     # Keep shrinking to check valid smaller windows
            return res
        
        return atleastK(k) - atleastK(k+1) # Main idea is since we can't find for exactly K, we find for atleast k and atleast k + 1, and then find the difference.