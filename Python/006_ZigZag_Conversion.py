"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            result = []
            for i in range(numRows):
                if ((i == 0) or (i == numRows-1)):
                    result.append(s[i::(numRows*2-2)])
                else:
                    for j in range(i, len(s), numRows*2-2):
                        result.append(s[j])
                        if ((j+numRows*2-2-2*i) < len(s)):
                            result.append(s[j+numRows*2-2-2*i])
            return "".join(result)