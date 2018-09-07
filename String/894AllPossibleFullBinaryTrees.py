# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N%2 == 0: return []
        def build(N):
            if N == 1:
                return [TreeNode(0)]
            res = []
            for i in range(1, N, 2):
                l,r = build(i), build(N-i-1)
                for left in l:
                    for right in r:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        return build(N)