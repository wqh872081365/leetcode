"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if amount >= min(coins):
            min_coins = min(coins)
            result = [-1] * (min_coins-1)
            for i in range(min_coins, amount+1):
                if i in coins:
                    result.append(1)
                else:
                    min_c = [result[i-coin-1] for coin in coins if coin < i and result[i-coin-1] != -1]
                    result.append(min(min_c)+1 if min_c else -1)
            return result[-1]
        else:
            return -1