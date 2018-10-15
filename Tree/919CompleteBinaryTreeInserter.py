class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter(object):
    def __init__(self, root):
        self.deque = []
        self.root = root
        q = [root]
        while q:
            node = q.pop(0)
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.pop(0)
        return node.val

    def get_root(self):
        return self.root


class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.queue = [self.root]
        for n in self.queue:
            if n.left: self.queue.append(n.left)
            if n.right: self.queue.append(n.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        new = TreeNode(v)
        self.queue.append(new)
        N = len(self.queue)
        parent = self.queue[N // 2 - 1]
        if not parent.left:
            parent.left = new
        else:
            parent.right = new
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root