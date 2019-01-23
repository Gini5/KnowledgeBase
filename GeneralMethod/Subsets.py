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

    def subsetsWithDup(self,nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Given a set of duplicate integers, nums, return all possible subsets (the power set).
        """
        nums.sort()
        res = [[]]
        for i, n in enumerate(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                for sub in self.subsetsWithDup(nums[i + 1:]):
                    res.append([n] + sub)
        return res

    def subsets2(self,nums):
        res = []

        def dfs(nums, index, path):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i + 1, path + [nums[i]])

        dfs(nums, 0, [])
        return res

    def subsetsWithDup2(self,nums):
        res = []
        nums.sort()
        def dfs(nums,index,path):
            res.append(path)
            for i in range(index, len(nums)):
                if i == index or nums[i] != nums[i-1]:
                    dfs(nums, i+1, path+[nums[i]])

        dfs(nums, 0, [])
        return res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        return all permutation for distinct array
        """
        if not nums: return [[]]
        res = []
        for i, n in enumerate(nums):
            for sub in self.permute(nums[:i] + nums[i + 1:]):
                res.append([n] + sub)
        return res

    def permuteWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        array may contain duplicates
        """
        if not nums: return [[]]
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                for sub in self.permute(nums[:i] + nums[i + 1:]):
                    res.append([n] + sub)
        return res

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        candidates = [2,3,5], target = 8, A solution set is:
        [
          [2,2,2,2],
          [2,3,3],
          [3,5]
        ]
        """
        res = []
        candidates.sort()
        for i, n in enumerate(candidates):
            if n < target:
                for sub in self.combinationSum(candidates[:i + 1], target - n):
                    res.append([n] + sub)
            elif n == target:
                res.append([n])
            else:
                break
        return res