# 3217
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:


        numset = set(nums)

        dummy = ListNode(0,head)
        
        prev = dummy
        curr = head

        while curr:
            if curr.val in numset:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next