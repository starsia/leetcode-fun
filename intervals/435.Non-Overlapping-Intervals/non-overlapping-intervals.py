class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        # sort by ascending order
        intervals.sort(key=lambda x: x[1])
        smallest_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if smallest_end > intervals[i][0]:
                # overlap
                count += 1
            else:
                smallest_end = intervals[i][1]
            
        return count


