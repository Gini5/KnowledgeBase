class Solution:
    def minDeletionSize(self, A):
        """
        delete at least how many columns to make each column non-decreasing
        """
        if not A: return 0
        res = 0
        for j in range(len(A[0])):
            for i in range(1,len(A)):
                if A[i-1][j] > A[i][j]:
                    res += 1
                    break
        return res