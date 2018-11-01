class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        if m == 1: return A[0][0]
        for i in range(1,m):
            for j in range(m):
                if j == 0:
                    A[i][j] += min(A[i-1][j],A[i-1][j+1])
                elif j<m-1:
                    A[i][j] += min(A[i-1][j],A[i-1][j-1],A[i-1][j+1])
                else:
                    A[i][j] += min(A[i-1][j],A[i-1][j-1])
        return min(A[m-1])


class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)

        for row in range(1, m):
            A[row][0] += min(A[row - 1][0:2])
            for col in range(1, m - 1):
                A[row][col] += min(A[row - 1][col - 1:col + 2])
            A[row][m - 1] += min(A[row - 1][m - 2:m])

        return min(A[m - 1])
