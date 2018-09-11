# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def check(node):
            if not node: return 0
            res = 0
            if node.val == 1: res = 1
            l = check(node.left)
            r = check(node.right)
            if not l: node.left = None
            if not r: node.right = None
            res |= l
            res |= r
            return res

        dummy = TreeNode(1)
        dummy.left = root
        check(dummy)
        return dummy.left

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val: return None
        return root