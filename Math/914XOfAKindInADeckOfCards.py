from functools import reduce
import collections

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        def gcd(a, b):
            #greatest common divisor
            while b:
                a, b = b, a % b
            return a

        count = list(collections.Counter(deck).values())
        return reduce(gcd, count) > 1