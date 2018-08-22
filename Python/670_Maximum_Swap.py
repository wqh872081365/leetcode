"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))
        swap = 1
        for i, n in enumerate(num_list[:-1]):
            index = i+1
            max_num = num_list[i+1]
            for j, m in enumerate(num_list[i+2:], start=i+2):
                if m >= max_num:
                    index = j
                    max_num = m
            if n < max_num:
                num_list[index], num_list[i] = num_list[i], num_list[index]
                swap -= 1
            if swap <= 0:
                break
        return int("".join(num_list))
