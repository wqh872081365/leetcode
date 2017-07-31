"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        a1 = [p1[0] - p2[0], p1[1] - p2[1]]
        a2 = [p1[0] - p3[0], p1[1] - p3[1]]
        a3 = [p1[0] - p4[0], p1[1] - p4[1]]
        a4 = [p2[0] - p3[0], p2[1] - p3[1]]
        a5 = [p2[0] - p4[0], p2[1] - p4[1]]
        a6 = [p3[0] - p4[0], p3[1] - p4[1]]

        s = [a1[0] ** 2 + a1[1] ** 2, a2[0] ** 2 + a2[1] ** 2, a3[0] ** 2 + a3[1] ** 2, a4[0] ** 2 + a4[1] ** 2,
             a5[0] ** 2 + a5[1] ** 2, a6[0] ** 2 + a6[1] ** 2]
        s.sort()
        if s[0] == s[1] == s[2] == s[3] != 0 and s[4] == s[5] and s[0] * 2 == s[4]:
            return True
        else:
            return False