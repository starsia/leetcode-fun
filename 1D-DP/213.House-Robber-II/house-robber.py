class Solution:
    def rob(self, nums: list[int]) -> int:
        def helper(start, end):
            memo = [-1] * len(nums)
            def dp(i):
                if i > end:
                    return 0

                if memo[i] >= 0:
                    return memo[i]

                result = max(dp(i + 1), dp(i + 2) + nums[i])
                memo[i] = result

                return result
            return dp(start)

        if len(nums) == 1:
            return nums[0]

        return max(
            helper(0, len(nums) - 2), 
            helper(1, len(nums) - 1)
        )

