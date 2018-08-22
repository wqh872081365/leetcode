"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""


class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(B) % len(A) == 0:
            if B == A * (len(B) / len(A)):
                return len(B) / len(A)
        count = len(B) / len(A) + 1
        if B in A * count:
            return count
        elif B in A * (count + 1):
            return count + 1
        else:
            return -1
