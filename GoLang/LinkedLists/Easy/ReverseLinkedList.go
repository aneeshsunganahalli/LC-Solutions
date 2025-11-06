// 206
package Easy
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var prev *ListNode = nil
    var curr *ListNode = head

    if head == nil { return nil }
    for curr.Next != nil {
        temp := curr.Next
        curr.Next = prev
        prev = curr
        curr = temp
    }

    curr.Next = prev
    return curr
}
