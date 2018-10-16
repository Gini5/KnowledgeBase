class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        e, o = 0, 1
        l = len(A)
        while e<l or o<l:
            while e<l and A[e]%2 == 0: e += 2
            while o<l and A[o]%2 != 0: o += 2
            if e<l and o<l: A[e], A[o] = A[o], A[e]
            e += 2
            o += 2
        return A