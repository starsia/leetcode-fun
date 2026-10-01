"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict = {}

        if not head:
            return None
    
        original = head
        while head:
            next = None
            random = None
                
            temp = Node(head.val, next, random)
            dict[head] = temp
            head = head.next
            
        head = original 
        
        while head:
            original_next = head.next
            if original_next:
                dict[head].next = dict[original_next]
        
            original_random = head.random
            if original_random:
                dict[head].random = dict[original_random]
            
            head = head.next
            
        return dict[original]
