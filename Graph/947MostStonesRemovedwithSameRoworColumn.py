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


t = Solution()
print(t.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(t.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))