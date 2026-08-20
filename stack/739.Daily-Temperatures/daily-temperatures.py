class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [] # stores the index of temperatures

        for index, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                highest_temp_index = stack.pop()
                results[highest_temp_index] = index - highest_temp_index

            stack.append(index)

        return results

