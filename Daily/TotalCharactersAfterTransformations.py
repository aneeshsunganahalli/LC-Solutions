class Solution:
  def lengthAfterTransformations(self, s: str, t: int) -> int:

    N = len(s)
    mod = 10**9 + 7
    count = [0] * 26
    
    for i in range(N):
      count[ord(s[i]) - ord('a')] += 1  # Initializing the count of each character in the string s
    
    for _ in range(t):
      tempCount = [0] * 26
      tempCount[0] = count[25] # Shifting count of z to a
      tempCount[1] = count[25] # Shifting count of z to b
      for i in range(25):
        tempCount[i + 1] += count[i] % mod # Shifting count of letter to next letter
      count = tempCount
    
    res = 0
    for i in range(26):
      res += count[i] % mod
    return res % mod
