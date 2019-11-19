# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# 1. loop the price in the list. Record the minimum_price and calculate the difference between current_price and minimum_price.
# Time complexity: O(N)





class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float('inf'), 0
        for elem in prices:
            min_price = min(elem, min_price)
            profit = elem - min_price
            max_profit = max(max_profit, profit)
        return max_profit