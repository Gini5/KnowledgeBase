class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        l = len(deck)
        deck.sort()
        res = [i for i in range(l)]
        index = [i for i in range(l)]
        i = 0
        for i in range(l):
            res[index.pop(0)] = deck[i]
            if index: index.append(index.pop(0))
        return res