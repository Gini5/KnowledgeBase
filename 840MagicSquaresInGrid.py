class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def check(x, y):
            if grid[x - 1][y - 1] != 5: return False
            colsum = [0] * 3
            for i in range(x - 2, x + 1):
                rowsum = 0
                for j in range(y - 2, y + 1):
                    e = grid[i][j]
                    if e > 9 or e < 1: return False
                    rowsum += e
                    colsum[j - (y - 2)] += e
                if rowsum != 15: return False
            if colsum != [15, 15, 15]: return False
            if grid[x - 2][y - 2] + grid[x][y] != grid[x][y - 2] + grid[x - 2][y] != 15: return False
            return True

        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3: return 0
        res = 0
        for i in range(2, n):
            for j in range(2, m):
                res += check(i, j)
        return res