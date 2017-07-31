"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        number = 0
        str_max = ""
        for i in range(len(s)):
            if (s[i-number:i+1] == s[i-number:i+1][::-1]):
                str_max = s[i-number:i+1]
                number += 1
                continue
            if ((i-number-1)>=0 and (s[i-number-1:i+1] == s[i-number-1:i+1][::-1])):
                str_max = s[i-number-1:i+1]
                number += 2
        return str_max