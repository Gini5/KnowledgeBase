class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n,m = len(A),len(A[0])
        new = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(m):
            for i in range(n):
                new[j][i] = A[i][j]
        return new