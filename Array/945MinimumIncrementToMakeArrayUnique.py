class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        A.sort()
        for i in range(1, len(A)):
            if A[i - 1] >= A[i]:
                ans += A[i - 1] + 1 - A[i]
                A[i] = A[i - 1] + 1
        return ans