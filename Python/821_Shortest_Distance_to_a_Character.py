"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.

"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_list = [i for i, s in enumerate(S) if s == C]
        res = range(c_list[0], 0, -1)
        for i in range(len(c_list)-1):
            tem = c_list[i+1] - c_list[i]
            res.extend(range(0, tem / 2 + 1))
            if tem % 2:
                res.extend(range(tem / 2, 0, -1))
            else:
                res.extend(range(tem / 2 - 1, 0, -1))
        res.extend(range(0, len(S) - c_list[-1]))
        return res
