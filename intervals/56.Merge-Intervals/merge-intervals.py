class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort()
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                # overlapping
                end = max(end, intervals[i][1])
            else:
                # not overlapping
                output.append([start, end])

                start, end = intervals[i][0],  intervals[i][1]

        output.append([start, end])




        return output
