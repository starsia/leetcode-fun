class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we will need some bfs here. 
        # we need to count levels

        if not grid:
            return -1 

        rows, cols = len(grid), len(grid[0])
        DIR = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        minutes = 0
        fresh_oranges = 0

        queue = collections.deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        while queue:
            print(grid)

            for _ in range(len(queue)):
                coordinate = queue.popleft()

                for x, y in DIR:
                    dx, dy = coordinate[0] + x, coordinate[1] + y
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                        queue.append((dx, dy))
                        grid[dx][dy] = 2
                        fresh_oranges -= 1

            minutes += 1

        
        if fresh_oranges > 0:
            return -1

        return max(0, minutes - 1)
            
