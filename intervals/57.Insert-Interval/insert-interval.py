class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            output.append([intervals[i][0], intervals[i][1]])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            minStart = min(intervals[i][0], newInterval[0])
            maxStart = max(intervals[i][1], newInterval[1])
            newInterval[0], newInterval[1] = minStart, maxStart
            i += 1

        output.append(newInterval)
        output.extend(intervals[i:])

        return output

