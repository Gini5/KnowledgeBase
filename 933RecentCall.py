class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.queue and self.queue[0]<t-3000:
            self.queue.pop(0)
        self.queue.append(t)
        return len(self.queue)