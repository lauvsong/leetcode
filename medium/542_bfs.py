class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        UNCACHED = -1
        m = len(mat)
        n = len(mat[0])
        
        dist = [[UNCACHED]*n for _ in range(m)]
        q = []
        
        for i,row in enumerate(mat):
            for j,cell in enumerate(row):
                if cell == 0:
                    q.append((i,j))
                    dist[i][j] = 0
                    
        dx = (-1,1,0,0)
        dy = (0,0,-1,1)
        level = 1
        while q:
            tmp = []
            
            for x,y in q:
                 
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if not (0 <= nx < m and 0 <= ny < n): continue
                    if dist[nx][ny] != UNCACHED: continue
                    if mat[nx][ny] == 1:
                        dist[nx][ny] = level
                        
                    tmp.append((nx,ny))
                
            level += 1
            q = tmp
            
        return dist
        
        
        
"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""