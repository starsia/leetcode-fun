class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        size = len(heights)
        stack = []

        for i, h in enumerate(heights):
            start = i # don't know if can extend back
            # check if the last value is greater than our value
            while stack and stack[-1][1] > h:
                iPrev, hPrev = stack.pop()
                # get the max area of the elem we just popped
                max_area = max(max_area, (i - iPrev) * hPrev)
                start = iPrev
            stack.append((start, h))

        # entries still in the stack
        for i, h in stack:
            max_area = max(max_area, (size - i) * h)

        return max_area

