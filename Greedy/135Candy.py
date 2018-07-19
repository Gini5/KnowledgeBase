# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 0: return 0

        c = [1] * n
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                c[i] = c[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                c[i - 1] = max(c[i - 1], c[i] + 1)

        return sum(c)