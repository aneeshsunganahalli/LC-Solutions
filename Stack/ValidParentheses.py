class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        hash = {")": "(", "}":"{","]":"["}  # Use hash to store closing and opening

        for c in s:
            if c in hash:
                if stack and stack[-1] == hash[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False