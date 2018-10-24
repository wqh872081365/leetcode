"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Note:

name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
"""


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if name[0] != typed[0]:
            return False
        t_l = len(typed)
        t_j = 0
        t_p = name[0]
        for i in name:
            if t_j >= t_l:
                return False
            if i == typed[t_j]:
                t_j += 1
                t_p = i
                continue
            else:
                while t_j < t_l and typed[t_j] == t_p:
                    t_j += 1
                if t_j >= t_l:
                    return False
                if i == typed[t_j]:
                    t_j += 1
                    t_p = i
                    continue
                else:
                    return False
        if t_j == t_l or all([t_p == typed[j] for j in range(t_j, t_l)]):
            return True
        else:
            return False
