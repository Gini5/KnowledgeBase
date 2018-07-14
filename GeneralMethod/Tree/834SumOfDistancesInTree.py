class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        col = collections.defaultdict(set)
        count = [0] * N
        res = [0] * N

        for l, r in edges:
            col[l].add(r)
            col[r].add(l)

        def dfs(root=0, seen=set()):
            seen.add(root)
            for n in col[root]:
                if n not in seen:
                    dfs(n, seen)
                    count[root] += count[n]
                    res[root] += res[n] + count[n]
            count[root] += 1

        def dfs2(root=0, seen=set()):
            seen.add(root)
            for n in col[root]:
                if n not in seen:
                    res[n] = res[root] - count[n] + N - count[n]
                    dfs2(n, seen)

        dfs()
        dfs2()
        return res