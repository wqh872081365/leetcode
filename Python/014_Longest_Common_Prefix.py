"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        list_str = sorted(strs)
        result = 0
        if len(list_str) == 0:
            return ""
        for i in range(min(len(list_str[0]), len(list_str[-1]))):
            if list_str[0][i] == list_str[-1][i]:
                result = i+1
            else:
                return list_str[0][:i]
        return list_str[0][:result]