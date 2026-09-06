class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        pts = []

        # python is a minheap. we actually want a max heap to 
        # pop the highest distance

        for x, y in points:
            distance = math.sqrt((x * x) + (y * y))
            pts.append([-distance, [x, y]])

        i = 0
        while i < len(pts):
            if len(arr) < k:
                heapq.heappush(arr, pts[i])
            else:
                lowest = heapq.heappop(arr)
                if -lowest[0] > -pts[i][0]:
                    # heapq.heappop(arr)
                    heapq.heappush(arr, pts[i])
                else: 
                    heapq.heappush(arr, lowest)
            i += 1

        output = []
        for i in arr:
            output.append(i[1])

        return output

