"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def judge(sub_str, pos, neg):
            if len(sub_str) == n * 2:
                result.append(sub_str)
            else:
                if pos < n:
                    judge(sub_str + "(", pos + 1, neg)
                if pos > neg:
                    judge(sub_str + ")", pos, neg + 1)

        judge("", 0, 0)
        return result
