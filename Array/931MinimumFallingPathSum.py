class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        """
        1 2 3
        4 5 6
        7 8 9
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