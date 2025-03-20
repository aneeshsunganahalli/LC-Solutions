class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        p = 16
        while p >= 0:            
            if n >= 3**p:
                n -= 3**p
            p -=1
            
            if n == 0:
                return True
        return False


# p = 16 as constraints are 1 <= n <= 10^7
