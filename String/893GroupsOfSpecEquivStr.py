class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        cnt = 0
        col = set()
        for a in A:
            split = (''.join(sorted(a[::2])),''.join(sorted(a[1::2])))
            if split not in col:
                col.add(split)
                cnt += 1
        return cnt