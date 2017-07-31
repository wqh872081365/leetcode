"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            sum = 0
            for i in range(1, int(num**0.5)+1):
                if num%i == 0:
                    if num/i == i:
                        sum += i
                    else:
                        sum += (i + num/i)
            return num*2 == sum
        else:
            return False