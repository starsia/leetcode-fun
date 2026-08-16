class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        # step 1: loop through the grid
        # step 2: apply bfs to each element at each loop
        # step 3: return number of islands

        def bfs(row, col):
            queue = collections.deque()
            visited.add((row, col))

            queue.append((row, col))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                print(queue)
                r, c = queue.popleft()
                for x, y in directions:
                    row, col = r + x, c + y
                    print(row, rows)
                    print(col, cols)

                    if row in range(rows) and col in range(cols) and (grid[row][col] == 1) and (row, col) not in visited:
                        queue.append((row, col))
                        visited.add((row, col))

        print(range(rows), range(cols))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    islands += 1
                    bfs(row, col)

        return islands

