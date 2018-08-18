class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,K+1):
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]+1
            if dp[i][K] >= N: return i