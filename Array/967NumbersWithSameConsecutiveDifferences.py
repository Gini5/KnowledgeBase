"""
Return all non-negative integers of length N such that the 
absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading
 zeros except for the number 0 itself. For example, 01 has 
 one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 

Note:

1 <= N <= 9
0 <= K <= 9
"""

class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        res = []
        def help(prev, n):
            if n==0 and len(prev) == N: res.append(int(''.join(prev)))
            elif n>0:
                num = int(prev[-1])
                if num-K>=0:
                    help(prev+[str(num-K)],n-1)
                if K != 0 and num+K<=9:
                    help(prev+[str(num+K)],n-1)
        
        for i in range(1,10):
            help([str(i)],N-1)
        if N == 1: res.append(0)
        return res

t = Solution()
print(t.numsSameConsecDiff(3,7))
print(t.numsSameConsecDiff(2,1))
print(t.numsSameConsecDiff(1,0))
print(t.numsSameConsecDiff(2,0))