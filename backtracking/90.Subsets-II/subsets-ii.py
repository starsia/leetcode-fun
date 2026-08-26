class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        output = []
        nums.sort()

        def track(index):
            if index == len(nums):
                output.append(subset.copy())
                return
            
            subset.append(nums[index])
            track(index + 1)
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            track(index + 1)

        track(0)
        return output
