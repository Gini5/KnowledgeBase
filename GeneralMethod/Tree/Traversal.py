# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorder(self,root):
        if not root: return []
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def inorder(self,root):
        if not root: return []
        return self.preorder(root.left) + [root.val] + self.preorder(root.right)

    def postorder(self,root):
        if not root: return []
        return self.preorder(root.left) + self.preorder(root.right) + [root.val]

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while True:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if not stack: return res
            root = stack.pop()
            root = root.right

    def inorderTraversal(self,root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack: return res
            root = stack.pop()
