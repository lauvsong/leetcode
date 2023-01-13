from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        START_COLOR = image[sr][sc]
        if START_COLOR == color:
            return image
        
        m = len(image)
        n = len(image[0])
        
        q = deque([(sr, sc)])
        cache = [[False]*n for _ in range(m)]
        
        dx = (-1,1,0,0)
        dy = (0,0,-1,1)
        
        while q:
            x,y = q.popleft()
            image[x][y] = color
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not (0<=nx<m and 0<=ny<n): continue
                if cache[nx][ny]: continue
                if image[nx][ny] != START_COLOR: continue
                
                cache[nx][ny] = True
                q.append((nx,ny))
        
        return image

"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
"""