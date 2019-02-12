class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        res = ""
        A.sort()
        for i in range(4):
            for j in range(i, 4):
                if i == 0:
                    if A[j] > A[i] and A[j] < 3: A[i], A[j] = A[j], A[i]
                if i == 1:
                    if A[0] == 0 or A[0] == 1: A[i], A[3] = A[3], A[i]
                    else:   #A[0] is 2