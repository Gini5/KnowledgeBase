class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        leftmax, maximum = A[0], A[0]
        partition = 0
        for i in range(1,len(A)):
            if leftmax>A[i]:   #left value doesn't fit condition 1
                partition = i
                leftmax = maximum
            else:
                maximum = max(A[i],maximum)
        return partition+1