/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return head;
        }

        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode temp = curr.next; // store the next node
            curr.next = prev; // assign prev to be next

            prev = curr; // since we're moving on, set curr to be prev
            curr = temp; // move curr to be the next node
        }

        return prev; // since curr is None at the end

        
    }
}
