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
        res, stack = [], []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

    def inorderTraversal(self,root):
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    def postorderTraversal(self,root):
        s1,s2 = [root], []
        res = []

        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left: s1.append(node.left)
            if node.right: s1.append(node.right)

        while s2:
            node = s2.pop()
            res.append(node.val)

        return res