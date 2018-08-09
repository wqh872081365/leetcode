"""
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # result = []
        # pairs.sort(key=lambda x: x[0])
        # for i, pair in enumerate(pairs):
        #     tem = None
        #     for j, pair_tem in enumerate(pairs[:i]):
        #         if pair_tem[1] < pair[0]:
        #             if tem:
        #                 tem = max(tem, result[j])
        #             else:
        #                 tem = result[j]
        #     if tem:
        #         result.append(tem + 1)
        #     else:
        #         result.append(1)
        # return result[-1] if result else 0

        result = 0
        pairs.sort(key=lambda x: x[1])
        if pairs:
            cur = pairs[0][1]
            result += 1
            for pair in pairs[1:]:
                if pair[0] > cur:
                    cur = pair[1]
                    result += 1
        return result
