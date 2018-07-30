"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_d = {}
        for i in s:
            if i in s_d:
                s_d[i] += 1
            else:
                s_d[i] = 1
        s_l = s_d.values()
        result = 0
        single = False
        for i in s_l:
            if i % 2:
                if not single:
                    single = True
                result += i - 1
            else:
                result += i
        return result + 1 if single else result
