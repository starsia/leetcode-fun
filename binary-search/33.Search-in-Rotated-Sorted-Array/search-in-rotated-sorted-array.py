class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while (start <= end):
            mid = (start + end) // 2
            print(search, start, mid, end)

            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]:
                print(' left side is sorted')
                if nums[start] <= target and nums[mid] > target: 
                    # search left
                    end = mid - 1
                    print('search left')
                else:
                    # search right
                    start = mid + 1
                    print(search right)

            else:
                print('right side sorted')
                # right side is sorted
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                    print('search right')
                else:
                    end = mid - 1
                    print('search left')


        return -1


