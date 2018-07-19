"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # import string
        # strs_dict = {}
        # for s in strs:
        #     s_dict = {s: 0 for s in string.ascii_lowercase}
        #     for sub_s in s:
        #         s_dict[sub_s] += 1
        #     s_dump = tuple(s_dict.values())
        #     if s_dump in strs_dict:
        #         strs_dict[s_dump].append(s)
        #     else:
        #         strs_dict[s_dump] = [s]
        # return strs_dict.values()

        strs_dict = {}
        for s in strs:
            s_dump = tuple(sorted(s))
            if s_dump in strs_dict:
                strs_dict[s_dump].append(s)
            else:
                strs_dict[s_dump] = [s]
        return strs_dict.values()
