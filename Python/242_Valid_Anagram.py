"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        for i in s:
            if s_dict.get(i):
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for j in t:
            if s_dict.get(j):
                s_dict[j] -= 1
            else:
                return False
        for k, v in s_dict.items():
            if v != 0:
                return False
        return True