from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        d = 0
        i = 0
        s = []
    
        while i < len(traversal):
            if traversal[i] == "-":
                d += 1
                i += 1
            else:
                j = i
                while j < len(traversal) and traversal[j] != "-":
                    j += 1
                node = TreeNode(int(traversal[i:j]))

                while len(s) > d:
                    s.pop()
                
                if s and not s[-1].left:
                    s[-1].left = node
                elif s:
                    s[-1].right = node

                s.append(node)

                d = 0
                i = j
        return s[0]