class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]

        if len(cost) == 2:
            return min(prev1, prev2)

        for i, v in enumerate(cost[2:]):
            if prev2 < prev1:
                temp = prev1
                prev1 = prev2 + v
                prev2 = temp

            else:
                temp = prev1
                prev1 = prev1 + v
                prev2 = temp
            
        return min(prev1, prev2)

