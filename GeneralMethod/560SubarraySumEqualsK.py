import collections
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, sm, sums = 0, 0, collections.defaultdict(int)
        for a in nums:
            sm += a
            res += sums[sm - k] + (sm == k)
            sums[sm] += 1
        return res