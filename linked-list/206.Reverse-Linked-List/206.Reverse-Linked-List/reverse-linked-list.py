# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time complexity here is O(n) for traversing the linkedlist once
        # space complexity is O(1) for only storing 3 variables and reversing in-place

        if head is None:
            return head

        # prev here is actually the last element in the linkedlist we will create
        prev = None

        temp = head
        while temp:
            originalNext = temp.next # this stores the original next element
            temp.next = prev # this assigns what came before to what comes after. 

            prev = temp # save the current to be used in the next loop
            temp = originalNext # we keep the loop going in the original order

        return prev # return prev and not temp because temp is currently None (it's actually the last element)
            


