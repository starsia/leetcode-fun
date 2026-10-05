class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next= next

class LRUCache:
    def __init__(self, capacity: int): 
        self.hashmap = {} 
        self.capacity = capacity 
        self.head = None 
        self.tail = None
        
    def add(self, key, value):
        temp = self.head 
        new = Node(key, value, None, temp)

        if self.head is None:
            self.head = new
            self.tail = new
        
        else:
            self.head.prev = new #added
            self.head = new #added

        self.hashmap[key] = new

        return new
            
    def delete(self, key): 
        if key in self.hashmap:
            temp = self.hashmap[key]
            temp_prev = temp.prev
            temp_next = temp.next
            
            # is vs == None

            if temp_prev is None and temp_next is None:
                # only node
                self.head = None
                self.tail = None

            elif temp_prev is None:
                # its at start
                self.head = self.head.next
                self.head.prev = None
                
            elif temp_next == None:
                # tail
                self.tail = self.tail.prev
                self.tail.next = None
                
            else:
                # middle
                temp_prev.next = temp_next
                temp_next.prev = temp_prev

            del self.hashmap[key]
            

    def get(self, key: int) -> int:
        if key in self.hashmap:
            val = self.hashmap[key].val

            self.delete(key)
            self.add(key, val)

            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.delete(key)
            self.add(key, value)

        else:
            if len(self.hashmap) == self.capacity:
                self.delete(self.tail.key)

            self.add(key, value)

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




