def findRedundantConnection(edges):
    def find(t):
        if t != p[t]:
            p[t] = find(p[t])
        return p[t]

    p = [0 for _ in range(100)]
    for i in range(100):
        p[i] = i

    for u,v in edges:
        if find(u) == find(v): return [u,v]
        else:
            p[find(u)] = find(v)


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        UF = {}

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in stones:
            union(i, ~j)

        return n - len({find(x) for x in UF})

t = Solution()
print(t.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))