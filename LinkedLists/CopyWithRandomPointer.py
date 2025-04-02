from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldToCopy = {None: None} # Hashmap to relate original to copies, defaulted to Null

        cur = head
        while cur:
            copy = Node(cur.val) # Creating node copy
            oldToCopy[cur] = copy   # Using current node as key for this copied node
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]   # Retrive node copy
            copy.next = oldToCopy[cur.next] # Assign next pointer
            copy.random = oldToCopy[cur.random] # Assign random pointer

            cur = cur.next
        
        return oldToCopy[head] # We can directly return head from hash