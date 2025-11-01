// 3217
package medium
// * Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func modifiedList(nums []int, head *ListNode) *ListNode {

	numSet := make(map[int]bool, len(nums))
	for _, val := range nums {
		numSet[val] = true
		if head.Val == val {
			head = head.Next
		}
	}

	dummy := &ListNode{Next: head}
	prev := dummy
	curr := head

	for curr != nil {
		if numSet[curr.Val] {
			prev.Next = curr.Next
			curr = curr.Next
		} else {
			prev = curr
			curr = curr.Next
		}
	}
	return dummy.Next
}
