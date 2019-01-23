class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Given a set of distinct integers, nums, return all possible subsets (the power set).
        """
        res = [[]]
        for i,n in enumerate(nums):
            for sub in self.subsets(nums[i+1:]):
                res.append([n]+sub)
        return res

    def subsets2(self,nums):
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)