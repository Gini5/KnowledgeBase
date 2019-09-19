    """
    Given an integer array arr and an integer k, modify the array by repeating it k times.

    For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

    Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

    As the answer can be very large, return the answer modulo 10^9 + 7.
    """
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def maxSumSubarrOfArr(arr):
            res = 0
            cur = 0
            for item in arr:
                cur = max(cur+item, item)
                res = max(res, cur)
            return res
        
        mod = 10**9+7
        res = 0
        if k > 1:
            # if k>1, consider if sum of arr>0, if yes,res = middle k-2 array sum + max(left + right)
            # if sum of arr <= 0, only need to consider max(left + right)
            midSum = (k-2)*sum(arr)
            if midSum < 0: midSum = 0
            res = midSum + maxSumSubarrOfArr(arr*2)
        else:
            # only need to consider arr's max sum of sub array
            res = maxSumSubarrOfArr(arr)
        return res