class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        while A:
            a = A[0]
            if a < 0:
                if a%2 != 0: return False
                if a // 2 in A:
                    A.remove(a//2)
                    A.remove(a)
                else: return False
            elif a > 0:
                if a * 2 in A:
                    A.remove(a*2)
                    A.remove(a)
                else: return False
            else:
                A.remove(a)
                if a in A: A.remove(a)
                else: return False

        return True

t = Solution()
print(t.canReorderDoubled([1,2,4,8]))