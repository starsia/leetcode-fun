# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head 
        fast = head
        before_middle = head

        while fast and fast.next:
            before_middle = slow
            slow = slow.next
            fast = fast.next.next

        def reverseList(link: ListNode | Node) -> ListNode | None:
            if not link:
                return None
                
            prev = None

            temp = link # we do this so we can preserve the pointer to the link, as temp will point
            # elsewhere after this
            while temp:
                originalNext = temp.next
                temp.next = prev

                prev = temp
                temp = originalNext

            return prev


        reversed = reverseList(slow)
        print(reversed)
        output = head

        while reversed:
            temp_front = head.next

            if not reversed.next:
                head.next = temp_front
                break

            temp_back = reversed.next

            head.next = reversed
            reversed.next = temp_front

            reversed = temp_back
            head = temp_front

        return output


