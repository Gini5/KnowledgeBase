# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTreeFromPOIO(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(pre,ino):
            if not pre: return
            root = TreeNode(pre[0])
            position = ino.index(pre[0])
            root.left = build(pre[1:position+1],ino[:position])
            root.right = build(pre[position+1:],ino[position+1:])
            return root

        return build(preorder,inorder)

    def buildTreeFromIOPO(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        root.left = self.buildTreeFromIOPO(inorder[:idx],postorder[:idx])
        root.right = self.buildTreeFromIOPO(inorder[idx+1:],postorder[idx:-1])
        return root


    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        #construct binary search tree from preorder list
        if not preorder: return
        root = TreeNode(preorder[0])
        i = 1
        while i<len(preorder):
            if preorder[i]>root.val: break
            else: i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root