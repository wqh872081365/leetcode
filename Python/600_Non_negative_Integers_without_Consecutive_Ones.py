"""
Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:
Input: 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
Note: 1 <= n <= 109
"""

import operator


class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """

        def c(n, k):
            if n >= k:
                if k > n - k:
                    k = n - k
                if k == 0:
                    return 1
                else:
                    return reduce(operator.mul, range(n - k + 1, n + 1)) / reduce(operator.mul, range(1, k + 1))
            else:
                return 0

        result = num + 1
        bin_num = bin(num)[2:][::-1]
        for i in range(len(bin_num) - 1):
            if bin_num[i] == "1" and bin_num[i + 1] == "1":
                result -= 1
                break
        if len(bin_num) > 1 and bin_num[1] == "1":
            for i in range(2, len(bin_num) - 1):
                if bin_num[i] == "1" and bin_num[i + 1] == "1":
                    result -= 2
                    break
            if bin_num[0] == "1":
                if len(bin_num) > 2 and bin_num[2] == "1":
                    result -= 1
                elif len(bin_num) > 2 and bin_num[2] == "0":
                    for i in range(3, len(bin_num) - 1):
                        if bin_num[i] == "1" and bin_num[i + 1] == "1":
                            result -= 1
                            break
        elif len(bin_num) > 1 and bin_num[1] == "0" and bin_num[0] == "1":
            for i in range(2, len(bin_num) - 1):
                if bin_num[i] == "1" and bin_num[i + 1] == "1":
                    result -= 1
                    break
        for i in range(2, len(bin_num)):
            if bin_num[i] == "1":
                for j in range(i + 1, len(bin_num) - 1):
                    if bin_num[j] == "1" and bin_num[j + 1] == "1":
                        result -= (2 ** i)
                        break
                else:
                    result -= (2 ** i - 1 - sum([c(j, i + 1 - j) for j in range(1, i + 1)]))
        return result