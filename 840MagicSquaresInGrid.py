class Solution(object):
    def numMagicSquaresInside(self, grid):
        R, C = len(grid), len(grid[0])
        ans = 0
        numbers = [x for x in range(1, 10)]
        
        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == numbers and
                (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))

        for r in range(R-2):
            for c in range(C-2):
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]): ans += 1
        return ans

        
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