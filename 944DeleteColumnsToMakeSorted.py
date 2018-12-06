class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A: return 0
        res = 0
        for j in range(len(A[0])):
            for i in range(1,len(A)):
                if A[i-1][j] > A[i][j]:
                    res += 1
                    break
        return res