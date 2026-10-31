class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        if(len(prices)<2):
            return 0
        min_price = prices[0]
        for price in prices[1:]:
            min_price = min(price,min_price)
            profit = price-min_price
            maxProfit = max(profit,maxProfit)
        return maxProfit
            
