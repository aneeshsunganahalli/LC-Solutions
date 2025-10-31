# 8
class Solution:
    def myAtoi(self, s: str) -> int:
        
        # Simplified
        string = s.lstrip()
        if not string: return 0

        i = 0
        res = 0
        sign = 1

        if string[i] == '-':
            sign = -1
            i += 1
        elif string[i] == "+":
            i += 1
        
        while i < len(string) and string[i].isdigit():
            res = res * 10 + int(string[i])
            if res * sign > 2**31 - 1:
                return 2**31 - 1
            if res * sign < -2**31:
                return -2**31
            i += 1
        return res * sign

        # Solution Somehow Passed
        i = 0
        sign = 1
        res = 0
        string = s.lstrip()
        n = len(string)
        started = False
        signSeen = False
        while i < n:
            if not signSeen and not started and string[i] == '-':
                sign = -1 
                i += 1
                signSeen = True
            elif not signSeen and not started and string[i] == '+':
                i += 1
                signSeen = True
            
            elif not started and signSeen and (string[i] == '+' or string[i] == '-'):
                return 0

            elif string[i].isdigit():
                started = True
                res = res * 10 + int(string[i])
                if res * sign > 2**31 - 1:
                    return 2**31 - 1
                elif res * sign < -2**31:
                    return -2**31
                i += 1
            else:
                break
        return res * sign