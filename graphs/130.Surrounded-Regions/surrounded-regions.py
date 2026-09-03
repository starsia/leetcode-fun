class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """ Do not return anything, modify board in-place instead. """
        rows, cols = len(board), len(board[0]) 
        DIR = [(1,0),(-1,0),(0,-1),(0,1)]

        def dfs(x, y):
            queue = collections.deque()
            queue.append((x, y))
            board[x][y] = '#'
            
            while queue:
                row, col = queue.popleft()
                for rowShift, colShift in DIR:
                    dx, dy = rowShift + row, colShift + col
                    if 0 <= dx < rows and 0 <= dy < cols and board[dx][dy] == 'O':
                        board[dx][dy] = '#'
                        queue.append((dx, dy))
            
        # we take only the edges here
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
            
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == '#':
                    board[i][j] = 'O'
