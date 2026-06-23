class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # time complexity of in-place sort is O(n log n), the two pointers method does O(n^2)
        # which dominates the in-place sort. 

        # space complexity is O(n^2) if we include the output. 
        # since there are only O(n^2) pairs, there can be at most O(n^2) unique solutions.
        # excluding output array it would be O(1)

        nums.sort()
        output = []
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1

                elif sum > 0:
                    right -= 1

                elif sum == 0: 
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return output

