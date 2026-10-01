# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        l1_int = int(0) 
        digits = 0
        
        while l1:
            temp = l1.val * (10 ** digits)
            l1_int += temp
            
            l1 = l1.next
            digits += 1
            
        l2_int = int(0)
        digits = 0
        
        while l2:
            temp = l2.val * (10 ** digits)
            l2_int += temp
            
            l2 = l2.next
            digits += 1
            
        total = l1_int + l2_int

        head = ListNode()
        output = head

        while total != 0:
            digit = total % 10

            head.val = int(digit)
            total = total // 10

            if total > 0 :
                head.next = ListNode()
                head = head.next

        return output

