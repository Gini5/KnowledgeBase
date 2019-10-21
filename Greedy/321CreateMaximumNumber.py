"""
Given two arrays of length m and n with digits 0-9 representing two numbers. 
Create the maximum number of length k <= m + n from digits of the two. 
The relative order of the digits from the same array must be preserved. 
Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxk(arr,i):
            res = []
            drop = len(arr) - i
            for e in arr:
                if not res: res.append(e)
                else:
                    while drop and res and res[-1]<e:
                        res.pop()
                        drop -= 1
                    res.append(e)
            return res[:i]
        
        def merge(a,b):
            res = []
            while a and b:
                if a[0]>b[0]: res.append(a.pop(0))
                else: res.append(b.pop(0))
            if a: res += a
            if b: res += b
            return res
            
        can = []
        for i in range(k+1):
            if i<=len(nums1) and (k-i)<=len(nums2):
                can1 = maxk(nums1,i)
                can2 = maxk(nums2,k-i)
                can.append(merge(can1,can2))
        return max(can)