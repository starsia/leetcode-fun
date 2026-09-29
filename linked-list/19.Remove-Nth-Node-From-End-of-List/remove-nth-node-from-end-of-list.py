# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        def reverseList(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            
            while node:
                originalNext = node.next
                node.next = prev

                prev = node
                node = originalNext

            return prev

        reversed = reverseList(head)

        count = 1
        prev = None
        temp = reversed

        while reversed:
            if count == n:
                if prev:
                    prev.next = reversed.next
                else:
                    temp = reversed.next
                break
            count += 1

            prev = reversed
            reversed = reversed.next
            # print(reversed)

        return reverseList(temp)


