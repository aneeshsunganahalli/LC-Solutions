from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        node = ListNode(0, head) # Links to the head
        groupPrev = node    # To keep track of node before a group

        while True:
            kth = self.getKth(groupPrev, k)  # Gets the kth node
            if not kth:
                break   # Group too small to reverse
            groupNext = kth.next   # Keeps track of node after group

            prev, cur = kth.next, groupPrev.next    # prev is assigned to node after kth as after reversal we need it to point to next group
            while cur != groupNext: # Boundary condition, apply regular reversal
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = groupPrev.next
            groupPrev.next = kth    # Kth node becomes first node now so the og previous node points to it
            groupPrev = temp    # OG first node becomes last node which acts as previous node for next group

        return node.next 
    
    def getKth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur