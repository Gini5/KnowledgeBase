import bisect
class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.winners = []
        count = {}
        winner = -1
        for i, p in enumerate(persons):
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(winner, 0):
                winner = p
            self.winners.append(winner)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.winners[bisect.bisect(self.times, t) - 1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)