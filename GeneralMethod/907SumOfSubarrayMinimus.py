class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int

        Input: [3,1,2,4]
        Output: 17
        Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
        Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

        for 3 as minimal, it's reponsible for [3]
        for 1 as minimal, it is responsible for [3,1,2,4]
        for 2, it's [2,4]
        for 4, it's [4]
        so the sum is sum([n*(i-left_boundary)*(right_boundary-i) for n in A]
        left boundary is cur-stack[-1], right boundary is i-cur
        """
        s = 0
        stack = []
        A = [float('-inf')] + A + [float('-inf')]
        for i, n in enumerate(A):
            while stack and n < A[stack[-1]]:
        # if stack's top element is bigger than n, top is not left boundary for n while top reaches its right boundary
                cur = stack.pop()
                s += A[cur]*(cur-stack[-1])*(i-cur) # calculate for top element since it reaches its right boundary
            stack.append(i)
        return s%(10**9+7)