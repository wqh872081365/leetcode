"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_tem = s+"#"+s[::-1]
        r = [0]
        for i in range(1, len(s_tem)):
            t = r[i-1]
            while t > 0 and s_tem[t] != s_tem[i]:
                t = r[t-1]
            if s_tem[t] == s_tem[i]:
                t += 1
            r.append(t)
        return s[r[-1]:][::-1]+s[::]