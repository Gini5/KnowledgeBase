"""
Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].

 

Example 1:



Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:



Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:



Input: root = [1,2,3], voyage = [1,2,3]
Output: []
 

Note:

1 <= N <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        res = []
        def dfs(node):
            if voyage and node:
                if voyage[0] == node.val:
                    voyage.pop(0)
                    if not dfs(node.left) or not dfs(node.right):
                        node.left, node.right = node.right, node.left
                        res.append(node.val)
                        if not dfs(node.left) or not dfs(node.right): return False
                        else: return True
                    else:
                        return True
                else: return False
            else: return True
        
        if dfs(root):
            return res
        else:
            return [-1]

t = Solution()
n1 = TreeNode(1)
n1.left = TreeNode(2)
n1.right = TreeNode(3)
n1.left.left = TreeNode(4)
n1.left.right = TreeNode(5)
print(t.flipMatchVoyage(n1,[1,3,2,5,4]))
            