"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000

"""


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        a_l = len(A)
        if a_l >= 3:
            i = 1
            while i < a_l - 1 and A[i] > A[i - 1]:
                i += 1
            if i - 1 > 0 and i - 1 < a_l - 1:
                while i < a_l and A[i] < A[i - 1]:
                    i += 1
                if i == a_l:
                    return True
        return False
