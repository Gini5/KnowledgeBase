"""
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""
class Solution:
    def regionsBySlashes(self, grid):
        m, n = len(grid), len(grid[0])
        g = [[0 for _ in range(n*3)] for _ in range(m*3)]
        regions = 0

        def dfs(g,i,j):
            if i>=0 and j>=0 and i<len(g) and j<len(g[0]) and not g[i][j]:
                g[i][j] = 1
                dfs(g,i+1,j)
                dfs(g,i,j+1)
                dfs(g,i-1,j)
                dfs(g,i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '/': g[i*3+2][j*3] = g[i*3+1][j*3+1] = g[i*3][j*3+2] = 1
                elif grid[i][j] == "\\": g[i*3][j*3] = g[i*3+1][j*3+1] = g[i*3+2][j*3+2] = 1
        
        for i in range(len(g)):
            for j in range(len(g[0])):
                if not g[i][j]:
                    dfs(g,i,j)
                    regions += 1
        
        return regions
    
t = Solution()
# print(t.regionsBySlashes([" /","/ "]))
print(t.regionsBySlashes(["\\/","/\\"]))