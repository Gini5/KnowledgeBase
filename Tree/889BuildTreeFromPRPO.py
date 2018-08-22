# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre: return
        root = pre[0]
        idx = post.index(root)
        left, right = None, None
        if len(pre) > 1:
            lroot = pre[1]  # we suppose this is left node, it could be right node as well
            lidx = post.index(lroot)
            left = self.constructFromPrePost(pre[1:2 + lidx], post[:lidx + 1])
            if idx - lidx > 1:  # have right node
                rroot = pre[2 + lidx]
                ridx = post.index(rroot)
                right = self.constructFromPrePost(pre[2 + lidx:], post[lidx + 1:idx])

        node = TreeNode(root)
        node.left = left
        node.right = right
        return node