"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            return int(str(x)[::-1]) if int(str(x)[::-1]) < pow(2, 31) else 0
        else:
            return int(str(abs(x))[::-1])*-1 if int(str(abs(x))[::-1]) < pow(2, 31) else 0