from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Stack
        stack = [(p,q)]

        while stack:
            n1, n2 = stack.pop()

            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))
        return True
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        # Queue

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for i in range(len(q1)):

                node1, node2 = q1.popleft(), q2.popleft()

                if not node1 and not node2:
                    continue
                if not node1 or not node2 or node1.val != node2.val:
                    return False
                
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
        return True