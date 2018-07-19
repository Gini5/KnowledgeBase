class Solution(object):
    # Only one trasaction
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = float('-inf')
        for p in prices:
            profit = max(profit,buy+p)
            buy = max(buy,-p)
        return profit

    # Endless transaction
    def maxProfitEndlessTrasactions(self,prices):
        profit = 0
        buy = float('-inf')
        for p in prices:
            profit = max(profit, buy + p)
            buy = max(buy, profit-p)
        return profit

    # With Transaction Fee for each pair
    def maxProfitWithFee(self, prices, fee):
        profit = 0
        buy = float('-inf')
        for p in prices:
            profit = max(profit, p + buy)
            buy = max(buy, profit - p - fee)
        return profit