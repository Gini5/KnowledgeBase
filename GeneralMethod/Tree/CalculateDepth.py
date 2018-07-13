# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depth(node):
            if not node: return 0
            ld = depth(node.left)
            rd = depth(node.right)
            if ld == -1 or rd == -1: return -1
            if abs(ld - rd) > 1: return -1
            return max(ld, rd) + 1

        return depth(root) != -1