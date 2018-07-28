import random
class Solution:

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n, self.m = n_rows, n_cols
        self.reset()

    def flip(self):
        """
        :rtype: List[int]
        """
        res = random.randint(0, self.total)
        while res in self.used:
            res = random.randint(0, self.total)
        self.used.add(res)
        return [res//self.m, res%self.m]

    def reset(self):
        """
        :rtype: void
        """
        self.total = self.n * self.m - 1
        self.used = set()

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()