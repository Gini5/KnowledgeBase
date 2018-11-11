# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        s = 0
        if root:
            if L<=root.val<=R:
                s += root.val
            return s+self.rangeSumBST(root.left,L,R)+self.rangeSumBST(root.right,L,R)
        else:
            return s