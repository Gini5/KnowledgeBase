class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        n = len(piles)
        l,r = 1, max(piles)

        while l<r:
            k = (l + r)//2
            s = sum((piles[i]-1)//k for i in range(n))
            if s > H-n:
                l = k+1
            else:
                r = k
        return l