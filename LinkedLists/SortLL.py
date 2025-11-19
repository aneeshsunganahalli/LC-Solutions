# 148
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None: 
            return head
        
        def find_middle(head):
            slow, fast = head, head
            prev = None

            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None
            return head, slow
        
        def merge(l, r):
            dummy = ListNode(-1)
            tail = dummy

            while l and r:
                if l.val <= r.val:
                    tail.next = l
                    l = l.next
                else:
                    tail.next = r
                    r = r.next
                tail = tail.next

            if l:
                tail.next = l
            if r:
                tail.next = r

            return dummy.next
        
        def mergeSort(node):
            if node is None or node.next is None:
                return node
            
            left, right = find_middle(node)
            left = mergeSort(left)
            right = mergeSort(right)

            return merge(left, right)

        
        return mergeSort(head)
        
