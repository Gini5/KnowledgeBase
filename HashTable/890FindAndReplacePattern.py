class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for w in words:
            l,r = {},{}
            for i in range(len(w)):
                if w[i] in l and l[w[i]] != pattern[i]: break
                if pattern[i] in r and r[pattern[i]] != w[i]: break
                l[w[i]] = pattern[i]
                r[pattern[i]] = w[i]
                if i == len(w)-1: res.append(w)
        return res