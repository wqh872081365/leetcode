"""
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # result = 0
        # index = True
        # for i in s:
        #     if index:
        #         if i != " ":
        #             result += 1
        #             index = False
        #     else:
        #         if i == " ":
        #             index = True
        # return result

        return len(s.split())
