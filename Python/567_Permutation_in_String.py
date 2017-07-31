"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        dict_s1 = {}
        for i in s1:
            dict_s1[i] = dict_s1.get(i, 0) + 1
        dict_s2 = {}
        for i in s2[:len(s1)]:
            dict_s2[i] = dict_s2.get(i, 0) + 1
        for i in range(len(s2)-len(s1)+1):
            if i > 0:
                if dict_s2[s2[i-1]] > 1:
                    dict_s2[s2[i-1]] -= 1
                else:
                    del dict_s2[s2[i-1]]
                dict_s2[s2[i+len(s1)-1]] = dict_s2.get(s2[i+len(s1)-1], 0) + 1
            if dict_s1 == dict_s2:
                return True
        return False