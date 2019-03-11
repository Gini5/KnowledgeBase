class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        def compare(w1, w2):
            i = 0
            while i < len(w1) and i < len(w2):
                o1, o2 = order.index(w1[i]), order.index(w2[i])
                if o1 < o2:
                    return True
                elif o1 == o2:
                    i += 1
                else:
                    return False
            return i >= len(w1)

        for i, w in enumerate(words):
            if i + 1 < len(words):
                if not compare(w, words[i + 1]): return False
        return True