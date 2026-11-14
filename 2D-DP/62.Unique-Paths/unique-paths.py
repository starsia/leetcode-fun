class Solution:
    def uniquePaths(self, m: int, n: int, i = 0, j = 0, memo = []) -> int:

        # rows = [-1] * m
        # memo = [rows] * n

        memo = [[-1] * m for _ in range(n)]

        # we are not counting steps but number of paths to the finishing node 

        def dfs(i, j):
            # out of bounds
            if i >= m or j >= n:
                return 0

            # final spot
            if i == m - 1 or j ==  n - 1:
                return 1

            # if that has path has been taken before
            if memo[j][i] != -1:
                return memo[j][i]
            
            memo[j][i] = dfs(i + 1, j) + dfs(i, j + 1) 

            return memo[j][i]

        return dfs(0,0)
