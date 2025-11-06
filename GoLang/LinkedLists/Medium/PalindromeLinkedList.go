// 234
package Medium
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    
    if head == nil || head.Next == nil {
        return true
    }
    slow, fast := head, head
    for fast.Next != nil && fast.Next.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }
    // Slow is at the middle now
    
    var prev *ListNode
    curr := slow.Next
    for curr != nil {
        temp := curr.Next
        curr.Next = prev
        prev = curr
        curr = temp
    }
    // Prev is head of the reversed second half of the list now

    // Compare till length of the reversed list
    for prev != nil {
        if prev.Val != head.Val {
            return false
        }
        prev = prev.Next
        head = head.Next
    }
    return true
}
