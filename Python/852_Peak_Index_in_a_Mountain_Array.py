"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

"""


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A[1] <= A[0]:
            return 0
        for i in range(2, len(A)):
            if A[i] > A[i - 1]:
                continue
            elif A[i] < A[i - 1]:
                for j in range(i + 1, len(A)):
                    if A[j] < A[j - 1]:
                        continue
                    else:
                        return 0
                return i - 1
            else:
                return 0
        return 0
