class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = {} 
        queue = collections.deque() 
        for task in tasks: 
            if task in count: 
                count[task] += 1 
            else: 
                count[task] = 1

        heap = []
        time = 0

        # we realise that we dont have to track the key at all, 
        # we just have to track the count as the logic ensures
        # the cooldown period and distance
        
        for key, value in count.items():
            # heappush(heap, [-value, key])
            heappush(heap, -value)
            
        first = heappop(heap)
        queue.append([first + 1, time + n + 1])
        
        while heap:
            top = heappop(heap)
            
            if top[0] != 0:
                heappush(heap, top[0])
                
                if time >= queue[0][1]:
                    queue.popleft()
                    queue.append([top[0], time + n + 1])
            
            
            time += 1
            
        return time
            
