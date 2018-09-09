class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.A:
            if self.A[0]>n:
                self.A[0] -= n
                return self.A[1]
            else:
                n -= self.A[0]
                self.A.pop(0)
                res = self.A.pop(0)
                if n == 0: return res
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)