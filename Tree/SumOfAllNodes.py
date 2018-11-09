# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sumofallnodes(root):
    s = [0]
    def dfs(node):
        if node:
            s[0] += node.val
            dfs(node.left)
            dfs(node.right)

    dfs(root)
    return s[0]


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
print(sumofallnodes(a))