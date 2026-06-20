# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # time complexity O(n) for size of linkedlist
        # space complexity O(1) for two pointers
        if not head:
            return False

        slow = head
        fast = head.next

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False

