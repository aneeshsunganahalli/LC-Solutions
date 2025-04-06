from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checker(node):
            stack = [(node,subRoot)]

            while stack:
                n1, n2 = stack.pop()
                if not n1 and not n2:
                    continue
                if not n1 or not n2 or n1.val != n2.val:
                    return False
                stack.append((n1.left,n2.left))
                stack.append((n1.right,n2.right))
            return True
        
        if not subRoot:
            return True
        if not root:
            return False
        
        if checker(root):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))