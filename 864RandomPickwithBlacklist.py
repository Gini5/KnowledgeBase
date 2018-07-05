class Solution:
    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.n = N
        self.black = set(blacklist)
        self.cur = 0
        self.visited = set()

    def pick(self):
        """
        :rtype: int
        """
        while self.cur in self.black:
            self.cur += 1
        if self.cur < self.n:
            num = self.cur
            self.cur += 1
        else:
            num = self.visited.pop()
        self.visited.add(num)
        return num

        
        # Your Solution object will be instantiated and called as such:
        # obj = Solution(N, blacklist)
        # param_1 = obj.pick()