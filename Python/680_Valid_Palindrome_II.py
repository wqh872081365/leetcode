"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_len = len(s)
        for i in range(s_len/2):
            if s[i] != s[s_len-1-i]:
                if s[i+1:s_len-i] == s[i+1:s_len-i][::-1] or s[i:s_len-i-1] == s[i:s_len-i-1][::-1]:
                    return True
                else:
                    return False
        return True
