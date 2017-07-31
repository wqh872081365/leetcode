"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price_sub_list = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
        result = 0
        for price_sub in price_sub_list:
            if price_sub > 0:
                result += price_sub
        return result