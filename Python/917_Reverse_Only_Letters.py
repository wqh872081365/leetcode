"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""


import string
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letter_set = set(string.letters)
        res = list(S)
        j = len(S) - 1
        for i in range(len(S)):
            if res[i] in letter_set:
                while j >= 0:
                    if S[j] not in letter_set:
                        j -= 1
                    else:
                        break
                res[i] = S[j]
                j -= 1
        return "".join(res)
