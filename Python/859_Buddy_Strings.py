"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        tem = []
        a_set = set([])
        repeat = False
        if len(A) == len(B):
            for i in range(len(A)):
                if not repeat:
                    if A[i] in a_set:
                        repeat = True
                    else:
                        a_set.add(A[i])
                if A[i] != B[i]:
                    tem.append([A[i], B[i]])
                    if len(tem) > 2:
                        return False
                    elif len(tem) == 2:
                        if tem[0][0] != tem[1][1] or tem[0][1] != tem[1][0]:
                            return False
            if len(tem) == 1:
                return False
            elif len(tem) == 0:
                if repeat:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
