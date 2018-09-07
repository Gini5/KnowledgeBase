# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        dummy = TreeNode(0)
        res = dummy
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            dummy.right = TreeNode(root.val)
            dummy = dummy.right
            root = root.right
        return res.right