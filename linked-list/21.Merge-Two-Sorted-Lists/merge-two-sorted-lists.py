# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time complexity is O(m + n) since each node from both lists is processed exactly once.
        # Space complexity is O(m + n) because the recursive call stack can grow to the total number of nodes in the worst case.

        # We have to note that this way modifies the original lists rather than creating new nodes, if we wanted to not mutate the arguments then we'll just create dummy values.

        if list1 is None:
            return list2
        elif list2 is None: 
            return list1

        if list1.val > list2.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

