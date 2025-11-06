// 328
package medium

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func oddEvenList(head *ListNode) *ListNode {
    
    if head == nil || head.Next == nil {
        return head
    }
    
    odd, even := head, head.Next
    pos := true
    o, e := odd, even

    curr := even.Next
    for curr != nil {
        if pos {
            o.Next = curr
            o = o.Next
        } else {
            e.Next = curr
            e = e.Next
        }
        pos = !pos
        curr = curr.Next
    }
    e.Next = nil
    o.Next = even
    return odd
}
