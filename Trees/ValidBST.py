from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS
        if not root:
            return True
        q = deque([(root, float("-inf"), float("inf"))])
        
        while q:
            for _ in range(len(q)):
                node, minVal, maxVal = q.popleft()
                if not (minVal < node.val < maxVal):
                    return False
                if node.left:
                    q.append((node.left, minVal, node.val))
                if node.right:
                    q.append((node.right,node.val, maxVal))
        return True 
class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:       
        # DFS
        def valid(root, minVal, maxVal):
            if not root:
                return True
            
            if not (minVal < root.val < maxVal):
                return False
            
            return (valid(root.left, minVal, root.val)
            and valid(root.right, root.val, maxVal))
        
        return valid(root, float("-inf"), float("inf"))