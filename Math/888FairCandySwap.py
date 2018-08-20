class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dif = (sum(A)-sum(B))//2
        B = set(B)
        for a in set(A):
            if a-dif in B:
                return [a,a-dif]