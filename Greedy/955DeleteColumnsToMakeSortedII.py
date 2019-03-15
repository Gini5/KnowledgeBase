class Solution:
    def minDeletionSize(self, A):
        """
        delete at least how many columns to make each line in lexicographic order
        """
        if not A: return 0
        res = 0
        needCompare = [True] * len(A)
        for j in range(len(A[0])):
            tmp = needCompare[:]
            for i in range(1, len(A)):
                if A[i - 1][j] > A[i][j] and needCompare[i]:  # not lexicographic order
                    res += 1
                    needCompare = tmp  # if delete this column, previous needCompare status should be reset
                    break
                elif A[i - 1][j] < A[i][j]:
                    needCompare[i] = False
        return res

t = Solution()
# print(t.minDeletionSize(["xga","xfb","yfa"]))
# print(t.minDeletionSize(["zyx","wvu","tsr"]))
print(t.minDeletionSize(["doeeqiy","yabhbqe","twckqte"]))