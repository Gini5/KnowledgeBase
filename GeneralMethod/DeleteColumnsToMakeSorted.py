class Solution:
    def minDeletionSize(self, A):
        """
        delete at least how many columns to make each column non-decreasing  A[0[c]<=A[1][c]<=A[2][c]...
        """
        if not A: return 0
        res = 0
        for j in range(len(A[0])):
            for i in range(1,len(A)):
                if A[i-1][j] > A[i][j]:
                    res += 1
                    break
        return res

    def minDeletionSizeII(self, A):
        """
        delete at least how many columns, make each line in lexicographic order A[0]<=A[1]<=A[2]...
        """
        if not A: return 0
        res = 0
        needCompare = [True] * len(A)
        for j in range(len(A[0])):
            tmp = needCompare[:]
            for i in range(1, len(A)):
                if A[i - 1][j] > A[i][j] and needCompare[i]:  # not lexicographic order
                    res += 1
                    needCompare = tmp  # if delete this column, previous needCompare status should be reset
                    break
                elif A[i - 1][j] < A[i][j]:
                    needCompare[i] = False
        return res

    def minDeletionSizeIII(self, A):
        """
        delete at least how many columns to make character in every line in lexicographic order  A[r][0]<=A[r][1]<=A[r][2]...
        """
        if not A: return 0
        m,n = len(A), len(A[0])
        # dp[i] is till i column, max. increasing subsequence
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if all(A[k][i] >= A[k][j] for k in range(m)):
                    dp[i] = max(dp[i], dp[j]+1)
        return n-max(dp)