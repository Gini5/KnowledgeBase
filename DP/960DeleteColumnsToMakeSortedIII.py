class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """


t = Solution()
print(t.minDeletionSize(["babca","bbazb"]))   #3
print(t.minDeletionSize(["edcba"]))     #4
print(t.minDeletionSize(["ghi","def","abc"]))   #0