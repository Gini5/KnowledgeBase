import collections
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        col = collections.defaultdict(list)

        for f, t in sorted(tickets)[::-1]:
            col[f].append(t)

        res = []
        stack = ["JFK"]
        while stack:
            while col[stack[-1]]:
                stack.append(col[stack[-1]].pop())
            res.append(stack.pop())
        return res[::-1]