class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = 0
        for i in range(1, len(A)):
            dif = A[i] - A[i - 1]
            if not increase:
                if dif < 0:
                    increase = -1
                elif dif > 0:
                    increase = 1
            else:
                if increase < 0 and dif > 0 or increase > 0 and dif < 0: return False

        return True