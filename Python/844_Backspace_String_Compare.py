"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_i = len(S) - 1
        t_i = len(T) - 1
        while True:
            count = 0
            while count >= 0 and s_i >= 0:
                if S[s_i] == "#":
                    count += 1
                    s_i -= 1
                else:
                    count -= 1
                    if count >= 0:
                        s_i -= 1
            count = 0
            while count >= 0 and t_i >= 0:
                if T[t_i] == "#":
                    count += 1
                    t_i -= 1
                else:
                    count -= 1
                    if count >= 0:
                        t_i -= 1
            if s_i >= 0 and t_i >= 0 and S[s_i] == T[t_i]:
                s_i -= 1
                t_i -= 1
                continue
            elif s_i < 0 and t_i < 0:
                return True
            else:
                return False
