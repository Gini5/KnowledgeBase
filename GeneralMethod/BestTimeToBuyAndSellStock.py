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

    # with 1 cool down day after selling
    def maxProfitWithCooldown(self, prices):
        n = len(prices)
        if n < 2: return 0

        profit = [0 for _ in range(n)]
        buy = [float('-inf') for _ in range(n)]
        for i in range(n):
            if i == 0:
                buy[i] = -prices[i]  # first day: set buy to first price
            elif i == 1:
                profit[i] = max(profit[i - 1], prices[i] + buy[i - 1])  # compare to yesterday, decide sell or not
                buy[i] = max(buy[i - 1],
                             profit[i - 1] - prices[i])  # compare to yesterday's profit, decide buy new or not
            else:
                profit[i] = max(profit[i - 1], prices[i] + buy[i - 1])  # compare to yesterday, decide sell or not
                buy[i] = max(buy[i - 1], profit[i - 2] - prices[
                    i])  # compare to the day before yesterday's profit, decide buy or not
        return profit[-1]