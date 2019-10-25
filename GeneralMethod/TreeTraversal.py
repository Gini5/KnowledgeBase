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
        # res, stack = [], []
        # while root or stack:
        #     while root:
        #         res.append(root.val)
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     root = root.right
        # return res
        res, stack = [], [root]
        while stack:
            n = stack.pop()
            if n:
                res.append(n.val)
                stack += [child for child in (n.right,n.left)]
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
        # s = []
        # res = []
        # while root or s:
        #     while root:
        #         res.append(root.val)
        #         s.append(root)
        #         root = root.right
        #     root = s.pop()
        #     root = root.left
        # return res[::-1]
        res, stack = [], [root]
        while stack:
            n = stack.pop()
            if n:
                res.append(n.val)
                stack += [child for child in (n.left,n.right)]
        return res[::-1]

    def levelorderTraversal(self,root):
        stack = [root]
        res = []
        while root and stack:
            res.append([n.val for n in stack])
            stack = [kid for n in stack for kid in (n.left, n.right) if kid]
        return res

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = [root]
        res, tmp, child = [], [], []
        while root and stack:
            node = stack.pop(0)
            tmp.append(node.val)
            if node.left: child.append(node.left)
            if node.right: child.append(node.right)
            if not stack:
                res.append(tmp)
                stack = child
                tmp, child = [], []
        return res