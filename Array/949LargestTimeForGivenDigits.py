class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """

        def iter(a):
            if len(a) > 0:
                res = []
                for i, e in enumerate(a):
                    res += [[e] + sub for sub in iter(a[:i] + a[i + 1:])]
                return res
            else:
                return [[]]

        res = ["0", "0"]
        for item in iter(A):
            h = str(item[0]) + str(item[1])
            m = str(item[2]) + str(item[3])
            if h < "24" and m < "60":
                if h > res[0] or h >= res[0] and m > res[1]: res = [h, m]
        return res[0] + ":" + res[1] if res != ["0", "0"] else ""