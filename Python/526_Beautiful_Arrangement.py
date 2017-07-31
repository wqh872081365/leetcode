"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 ? i ? N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Note:
N is a positive integer and will not exceed 15.
"""


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.result = 0

        def count(N, index, N_list):
            if index > N:
                self.result += 1
            else:
                for i in range(1, N + 1):
                    if N_list[i] == 0 and (i % index == 0 or index % i == 0):
                        N_list[i] = 1
                        count(N, index + 1, N_list)
                        N_list[i] = 0

        if N == 0:
            return 0
        count(N, 1, [0] * (N + 1))
        return self.result