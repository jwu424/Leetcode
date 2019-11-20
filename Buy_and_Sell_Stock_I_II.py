# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# 1. loop the price in the list. Record the minimum_price and calculate the difference between current_price and minimum_price.
# Time complexity: O(N)

# 2. DP. Create a loc and record loc if loc+prices[i]-prices[i-1] > 0.
# Time complexity: O(N)




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = float('inf'), 0
        for elem in prices:
            min_price = min(elem, min_price)
            profit = elem - min_price
            max_profit = max(max_profit, profit)
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        loc = 0
        res = [loc]
        for i in range(1, len(prices)):
            loc = max(loc+prices[i]-prices[i-1], 0)
            res.append(loc)
        return max(res)
    
    def maxProfit3(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        res = [0] * len(prices)
        for i in range(1, len(prices)):
            res[i] = max(res[i-1]+prices[i]-prices[i-1], 0)
        return max(res)



# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# 1. Each time, compare the difference between price[i] and price[i-1], if it is greater than 0, then add to res.
# Time complexity: O(N)

# 2. Same idea, but more concise
# Time complexity: O(N)


class Solution2:
    def maxProfit1(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i]-prices[i-1], 0)
        return res

    def maxProfit2(self, prices: List[int]) -> int:
        return sum(b-a for a, b in zip(prices, prices[1:]) if b>a)