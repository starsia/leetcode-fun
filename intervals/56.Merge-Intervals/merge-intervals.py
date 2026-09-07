class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort() 
        queue = collections.deque(intervals)
        print(queue) 
        output = [] 
        start, end = queue.popleft()

        while queue:
            front, back = queue.popleft()
            if end < front:
                output.append([start, end])
                start, end = front, back
                continue
            # if front <= start < back:
            else: 
                end = max(end, back)

        output.append([start, end])
    
        return output
