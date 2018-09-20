class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        types = []
        res = 0
        collect = 0
        prev = []
        for i,t in enumerate(tree):
            if t in types: collect += 1
            else:
                if len(types) == 2:
                    res = max(res,collect)
                    types = [prev[0]]
                    types.append(t)
                    collect = prev[1]+1
                else:
                    types.append(t)
                    collect += 1
            if i == 0 or tree[i] != tree[i-1]: prev = [t,0]
            prev[1] += 1
        res = max(res,collect)
        return res

    def totalFruit2(self, tree):
        res = cur = count_b = a = b = 0
        for c in tree:
            cur = cur + 1 if c in (a, b) else count_b + 1
            count_b = count_b + 1 if c == b else 1
            if b != c: a, b = b, c
            res = max(res, cur)
        return res