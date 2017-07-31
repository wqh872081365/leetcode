"""
Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        index = 0
        pre = 0
        post = 0
        [s1, s2] = equation.split("=")
        for i in range(1, len(s1)):
            if s1[i] == "+" or s1[i] == "-":
                if "x" == s1[i-1]:
                    if s1[index:i-1] in ["", "+"]:
                        pre += 1
                    elif s1[index:i-1] == "-":
                        pre -= 1
                    else:
                        pre += int(s1[index:i-1])
                else:
                    post += int(s1[index:i])
                index = i
        if "x" == s1[-1]:
            if s1[index:-1] in ["", "+"]:
                pre += 1
            elif s1[index:-1] == "-":
                pre -= 1
            else:
                pre += int(s1[index:-1])
        else:
            post += int(s1[index:])
        index = 0
        for i in range(1, len(s2)):
            if s2[i] == "+" or s2[i] == "-":
                if "x" == s2[i-1]:
                    if s2[index:i-1] in ["", "+"]:
                        pre -= 1
                    elif s2[index:i-1] == "-":
                        pre += 1
                    else:
                        pre -= int(s2[index:i-1])
                else:
                    post -= int(s2[index:i])
                index = i
        if "x" == s2[-1]:
            if s2[index:-1] in ["", "+"]:
                pre -= 1
            elif s2[index:-1] == "-":
                pre += 1
            else:
                pre -= int(s2[index:-1])
        else:
            post -= int(s2[index:])
        if pre == 0:
            if post == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return "x=" + str(post/pre*-1)