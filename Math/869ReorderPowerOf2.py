import collections
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        c = collections.Counter(str(N))
        return any(c == collections.Counter(str(1 << i)) for i in range(30))