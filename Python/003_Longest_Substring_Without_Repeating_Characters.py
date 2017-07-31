"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result_len = 0
        result_str = ""
        for i in range(len(s)):
            if s[i] not in result_str:
                result_str += s[i]
                result_len = len(result_str) if result_len < len(result_str) else result_len
            else:
                index = result_str.index(s[i])
                result_str = result_str[index+1:]
                result_str += s[i]
        return result_len