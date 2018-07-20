# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
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