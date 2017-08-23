"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        index = 0
        number = ""
        for i in str:
            if index == 0:
                if i == " ":
                    pass
                elif i == "+":
                    index = 1
                elif i == "-":
                    index = -1
                elif i in "0123456789":
                    number += i
                    index = 1
                else:
                    break
            else:
                if i in "0123456789":
                    number += i
                else:
                    break
        if number:
            if index == 1:
                if int(number) < 2147483647:
                    return index * int(number)
                else:
                    return 2147483647
            elif index == -1:
                if int(number) < 2147483648:
                    return index * int(number)
                else:
                    return -2147483648
        else:
            return 0