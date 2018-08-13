class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            maxj = 0
            for j in range(n):
                if grid[i][j] != 0: res += 1  # for xy planes
                maxj = max(maxj, grid[i][j])
            res += maxj  # for xz planes

        for j in range(n):
            res += max([grid[i][j] for i in range(m)])  # for yz planes

        return res