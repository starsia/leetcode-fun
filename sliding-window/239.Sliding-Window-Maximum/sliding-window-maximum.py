class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l = 0
        output = []

        # Brute force results in TLE
        # for r in range(k - 1, len(nums)):
        #     val = max(nums[l:r + 1], default = nums[0])
        #     output.append(val)
        #     l += 1

        # return output

        res = [0] * (len(nums) - k + 1)
        queue = collections.deque()

        for i in range(len(nums)):
            # front index fell out of the window so we can remove it
            if len(queue) > 0 and queue[0] <= i - k:
                queue.popleft()

            # back values smaller than nums[i] are useless so we can remove them
            while len(queue) > 0 and queue[-1] < nums[i]:
                queue.pop()

            queue.append(i)

            # window is full, so the front is the max
            if i >= k - 1:
                res[i - k + 1] = nums[queue[0]]

            # end state before last window looks like [3, -1, -3]

        return res
