class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        flipcnt, onecnt = 0, 0
        for c in S:
            if c == '0':
                if onecnt != 0: flipcnt += 1
            else:
                onecnt += 1
            if flipcnt > onecnt: flipcnt = onecnt
        return flipcnt