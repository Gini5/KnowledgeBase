import collections

class Solution:
    def removeStones(self, stones: 'List[List[int]]') -> 'int':
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for i,j in stones:
            rows[i].add(j)
            cols[j].add(i)

        def dfsRow(i):
            seenR.add(i)
            for j in rows[i]:
                if j not in seenC:
                    dfsCol(j)

        def dfsCol(j):
            seenC.add(j)
            for i in cols[j]:
                if i not in seenR:
                    dfsRow(i)

        seenR, seenC = set(), set()
        islands = 0
        for i, j in stones:
            if i not in seenR:
                islands += 1
                dfsRow(i)
                dfsCol(j)

        return len(stones)-islands

t = Solution()
print(t.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(t.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))