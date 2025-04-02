from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
       self.val = x
       self.next = None
       
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find middle of the array
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next  # Start of right part
        prev = slow.next = None

        # Reverse the right part
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge the two parts one by one
        first, second = head, prev
        while second:
            tp1, tp2 = first.next, second.next
            first.next = second
            second.next = tp1

            first, second = tp1, tp2