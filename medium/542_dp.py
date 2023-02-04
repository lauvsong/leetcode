class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        dist = [[float('inf')]*n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                else:
                    if 0 < r:
                        dist[r][c] = min(dist[r][c], dist[r-1][c] + 1)
                    if 0 < c:
                        dist[r][c] = min(dist[r][c], dist[r][c-1] + 1)
                    
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r < m-1:
                    dist[r][c] = min(dist[r][c], dist[r+1][c] + 1)
                if c < n-1:
                    dist[r][c] = min(dist[r][c], dist[r][c+1] + 1)
        
        return dist

"""
Intuition

The distance of a cell from 0 can be calculated if we know the nearest distance for all the neighbors, in which case the distance is the minimum distance of any neighbor + 1. And, instantly, the words that come to mind are Dynamic Programming (DP)!!
From each 1, the minimum path to 0 could be in any direction. So, we need to check all the 4 directions. In one iteration from top to bottom, we can check left and top directions, and we need another iteration from bottom to top to check for right and bottom directions.


Iterate over the matrix from top to bottom-left to right
"""