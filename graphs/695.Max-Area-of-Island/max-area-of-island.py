class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # step 1: iterate through the grid, 
        # apply dfs to each value
        # return highest count

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col) -> int:
            queue = collections.deque()
            
            queue.append((row, col))
            possible_largest = 1
            island = [(row, col)]

            direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in direction:
                    row, col = dr + r, dc + c


                    if row in range(rows) and col in range(cols) and (row, col) not in visited and grid[row][col] == 1:
                        visited.add((row, col))
                        possible_largest += 1
                        queue.append((row, col))
                        island.append((row, col))
                        
            return possible_largest

        max_area = 0


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))

                    max_area = max(max_area, bfs(row, col))

        return max_area

