class Solution:
    def jump(self, nums: List[int]) -> int:
        output = 0
        curr_range = 0
        max_range = 0
        
        for i in range(len(nums) - 1):
            max_range = max(i + nums[i], max_range)

            if i == curr_range:
                output += 1
                curr_range = max_range

        return output
