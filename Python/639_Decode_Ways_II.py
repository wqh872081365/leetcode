"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = 1000000007
        if s[0] == "0":
            return 0
        result = [1, 9 if s[0] == "*" else 1]
        for i in range(1, len(s)):
            if s[i] == "*":
                if s[i-1] == "*":
                    result.append((result[-1]*9+result[-2]*15)%M)
                elif s[i-1] == "0":
                    result.append((result[-1]*9)%M)
                elif s[i-1] == "1":
                    result.append((result[-1]*9+result[-2]*9)%M)
                elif s[i-1] == "2":
                    result.append((result[-1]*9+result[-2]*6)%M)
                else:
                    result.append((result[-1]*9)%M)
            elif s[i] == "0":
                if s[i-1] == "*":
                    result.append((result[-2]*2)%M)
                elif s[i-1] in ["1", "2"]:
                    result.append((result[-2])%M)
                else:
                    result.append(0)
            elif s[i] in ["7", "8", "9"]:
                if s[i-1] in ["*", "1"]:
                    result.append((result[-1]+result[-2])%M)
                else:
                    result.append((result[-1])%M)
            else:
                if s[i-1] == "*":
                    result.append((result[-1]+result[-2]*2)%M)
                elif s[i-1] in ["1", "2"]:
                    result.append((result[-1]+result[-2])%M)
                else:
                    result.append((result[-1])%M)
        return result[-1]