"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        s_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                s_stack.append(i)
            else:
                if len(s_stack) > 0 and s[s_stack[-1]] == "(":
                    s_stack.pop()
                    if len(s_stack) > 0:
                        result = max(result, i-s_stack[-1])
                    else:
                        result = max(result, i+1)
                else:
                    s_stack.append(i)
        return result