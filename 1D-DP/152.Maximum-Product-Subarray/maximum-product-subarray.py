
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = curr_min = curr_max = nums[0]

        for num in nums[1:]:
            if num < 0:
                curr_min, curr_max = curr_max, curr_min

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            res = max(res, curr_max)

        return res

'''
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1
        for num in nums:
            if num == 0:
                curr_min, curr_max = 1, 1
                continue
            
            tmp = curr_min * num
            curr_min = min(curr_min * num, curr_max * num, num)
            curr_max = max(curr_max * num, tmp, num)
            res = max(curr_max, res)
            
            
            
        return res
'''
