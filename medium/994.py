class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN = 2
        IMPOSSIBLE = -1
        CACHED = -2

        ROW_LEN = len(grid)
        COL_LEN = len(grid[0])

        DX = (0,0,-1,1)
        DY = (-1,1,0,0)

        rottens = []
        fresh_cnt = 0

        def bfs(q, fresh_cnt):
            minute = 0

            while q:
                childs = []

                for x, y in q:

                    for i in range(4):
                        nx = x + DX[i]
                        ny = y + DY[i]

                        if 0 <= nx < ROW_LEN and 0 <= ny < COL_LEN:
                            if grid[nx][ny] != FRESH:
                                continue

                            grid[nx][ny] = CACHED
                            childs.append((nx,ny))
                            fresh_cnt -= 1

                q = childs
                if q:
                    minute += 1

            return minute if fresh_cnt == 0 else IMPOSSIBLE
        

        for row in range(ROW_LEN):
            for col in range(COL_LEN):

                if grid[row][col] == ROTTEN:
                    rottens.append((row, col))
                
                if grid[row][col] == FRESH:
                    fresh_cnt += 1

        return bfs(rottens, fresh_cnt)


"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""