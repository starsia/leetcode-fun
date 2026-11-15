class Solution:
    def uniquePaths(self, m: int, n: int, i = 0, j = 0, memo = []) -> int:
        memo = [[0] * n for _ in range(m)]

        # destination
        memo[m - 1][n - 1] = 1

        for y in range(m - 1, -1, -1):
            for x in range(n - 1, -1, -1):

                # out of bound
                if m < y or n < x:
                    return 

                # something valid below
                if y + 1 < m:
                    memo[y][x] += memo[y + 1][x]
        
                # something valid to right
                if x + 1 < n:
                    memo[y][x] += memo[y][x + 1]
                
        return memo[0][0]
