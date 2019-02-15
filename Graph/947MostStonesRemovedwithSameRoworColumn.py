import collections

class Solution:
    def removeStones(self, stones: 'List[List[int]]') -> 'int':
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for i,j in stones:
            rows[i].add(j)
            cols[j].add(i)

        def dfs(i,j):
            visited.add((i,j))
            for c in rows[i]:
                if (i,c) not in visited:
                    dfs(i,c)

            for r in cols[j]:
                if (r,j) not in visited:
                    dfs(r,j)

        visited = set()
        islands = 0
        for i, j in stones:
            if (i,j) not in visited:
                islands += 1
                dfs(i,j)

        return len(stones)-islands

    def removeStoneUF(self, stones):
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

        return len(stones) - len({find(x) for x in UF})

t = Solution()
# print(t.removeStoneUF([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(t.removeStoneUF([[0,1],[1,0],[1,2],[2,1],[2,2]]))