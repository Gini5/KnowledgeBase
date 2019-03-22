class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A: return 0
        # dp[i] is till i column, max. increasing subsequence
        dp = [0 for _ in range(len(A[0]))]
        for i in range(1,)

t = Solution()
print(t.minDeletionSize(["babca","bbazb"]))   #3
print(t.minDeletionSize(["edcba"]))     #4
print(t.minDeletionSize(["ghi","def","abc"]))   #0


#babca
#bbazb