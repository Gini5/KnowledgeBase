class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]: res += 2 + 4*grid[i][j]
                if i: res -= min(grid[i][j],grid[i-1][j])*2
                if j: res -= min(grid[i][j],grid[i][j-1])*2
        return res