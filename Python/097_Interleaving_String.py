"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3)!=len(s1)+len(s2):
            return False
        s3_list = [[False for i in range(len(s1)+1)] for j in range(len(s2)+1)]
        s3_list[0][0] = True
        for i in range(1, len(s1)+1):
            s3_list[0][i] = True if s3_list[0][i-1] and s1[i-1]==s3[i-1] else False
        for i in range(1, len(s2)+1):
            s3_list[i][0] = True if s3_list[i-1][0] and s2[i-1]==s3[i-1] else False
        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                s3_list[i][j] = True if (s3_list[i][j-1] and s1[j-1]==s3[i+j-1]) or (s3_list[i-1][j] and s2[i-1]==s3[i+j-1]) else False
        return s3_list[len(s2)][len(s1)]