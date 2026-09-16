class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [-1] * len(nums)
        def helper(nums, i):
            if i < 0:
                return 0

            if memo[i] >= 0:
                return memo[i]

            result = max(helper(nums, i - 1), helper(nums, i - 2) + nums[i])
            memo[i] = result

            return result

        return helper(nums, len(nums) - 1)
                
