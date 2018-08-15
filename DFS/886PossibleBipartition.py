import collections
class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        group = [0 for i in range(N + 1)]  # group[i] == 0 means not grouped, 1 or -1 means group 1 or -1
        col = collections.defaultdict(list)
        for p1, p2 in dislikes:
            col[p1].append(p2)
            col[p2].append(p1)

        def dfs(index, togroup):
            group[index] = togroup
            for hate in col[index]:
                if group[hate] == togroup: return False
                if group[hate] == 0 and not dfs(hate, -togroup):
                    return False
            return True

        for i in range(1, N + 1):
            if group[i] == 0 and not dfs(i, 1):
                return False

        return True