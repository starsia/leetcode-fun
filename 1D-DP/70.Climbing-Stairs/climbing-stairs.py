class Solution:
    # def helper(x: int) -> int:
        # if x 
    def climbStairs(self, n: int) -> int:
        prev1 = 1 # takes 1 step to get from n to n
        prev2 = 1 # takes 1 step to get from n - 1 to n

        for i in range(n - 2, -1, -1):
            temp = prev1 + prev2
            prev1 = prev2
            prev2 = temp

        return prev2

