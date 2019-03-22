class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
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

t = Solution()
print(t.minDeletionSize(["babca","bbazb"]))   #3
print(t.minDeletionSize(["edcba"]))     #4
print(t.minDeletionSize(["ghi","def","abc"]))   #0


#babca
#bbazb