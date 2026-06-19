/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return head
    }

    var prev * ListNode = nil

    var temp = head

    for temp != nil {
        var curr *ListNode = temp.Next
        temp.Next = prev

        prev = temp
        temp = curr
    }

    return prev

}
