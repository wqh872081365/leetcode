"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        s_len = len(s)
        for i in range(s_len):
            tem = 1
            while i - tem >= 0 and i + tem <= s_len - 1 and s[i - tem] == s[i + tem]:
                tem += 1
            result += tem
        for i in range(s_len - 1):
            tem = 0
            while i - tem >= 0 and i + tem + 1 <= s_len - 1 and s[i - tem] == s[i + tem + 1]:
                tem += 1
            result += tem
        return result
