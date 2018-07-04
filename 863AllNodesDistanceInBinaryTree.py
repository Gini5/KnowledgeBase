# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        col = {}
        td = [-1]

        def dfs(node, dist):
            if node:
                if node.val == target: td[0] = dist
                col[node.val] = dist
                dfs(node.left, dist + 1)
                dfs(node.right, dist + 1)

        dfs(root, 0)
        return td[0]

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
t = Solution()
print(t.distanceK(t1,2,0))