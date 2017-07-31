"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        M = {"":0, "M":1, "MM":2, "MMM":3}
        C = {"":0, "C":1, "CC":2, "CCC":3, "CD":4, "D":5, "DC":6, "DCC":7, "DCCC":8, "CM":9}
        X = {"":0, "X":1, "XX":2, "XXX":3, "XL":4, "L":5, "LX":6, "LXX":7, "LXXX":8, "XC":9}
        I = {"":0, "I":1, "II":2, "III":3, "IV":4, "V":5, "VI":6, "VII":7, "VIII":8, "IX":9}
        result = re.match("^(M{0,3})(C{0,3}D{0,1}C{0,3}M{0,1})(X{0,3}L{0,1}X{0,3}C{0,1})(I{0,3}V{0,1}I{0,3}X{0,1})$", s)
        return M[result.group(1)]*1000 + C[result.group(2)]*100 + X[result.group(3)]*10 + I[result.group(4)]