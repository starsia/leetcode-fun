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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // time complexity is O(m + n) as shown in python file
        // we want to avoid doing this recursively because the recursive stack will get big.
        // how can we do this in O(1) space complexity? use dummy node as the first and return
        // dummy.next
        if (list1 == null) {
            return list2;
        }

        else if (list2 == null) {
            return list1;
        }

        ListNode dummy = new ListNode();
        ListNode head = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val > list2.val) {
                dummy.next = list2;
                list2 = list2.next;
            } else {
                dummy.next = list1;
                list1 = list1.next;
            }
            dummy = dummy.next;
        }

        if (list1 != null) {
            dummy.next = list1;
        } else {
            dummy.next = list2;
        }

        return head.next;

        
    }
}
