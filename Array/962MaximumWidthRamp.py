class Solution:
    def maxWidthRamp(self, A):
        n = len(A)
        res = 0
        for i in range(n):
            if n-1-i<res: break
            for j in range(i+1,n):
                if A[i]<=A[j]:
                    res = max(res,j-i)
        return res