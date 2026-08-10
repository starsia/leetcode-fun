class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # step 1: iterate through the grid, 
        # apply dfs to each value
        # return highest count

        if not grid:
            return 0

        # instead of having a 'visited' set, we can modify the grid
        # in-place to save some space complexity from O(island size) to O(1)

        rows, cols = len(grid), len(grid[0])
        # we also shift the direction list up to avoid creating at each bfs call
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs(row, col) -> int:
            queue = collections.deque()
            
            queue.append((row, col))
            possible_largest = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in direction:
                    row, col = dr + r, dc + c

                    # we can use a direct comparision which is arithmetic instead of 
                    # using the range method like row in range(rows) which creates
                    # an object every time
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        grid[row][col] = 0
                        possible_largest += 1
                        queue.append((row, col))
                        
            return possible_largest

        max_area = 0


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid[row][col] = 0

                    max_area = max(max_area, bfs(row, col))

        return max_area

