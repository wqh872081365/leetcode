"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a_dict = {}
        for a in A.split():
            if a in a_dict:
                a_dict[a] += 1
            else:
                a_dict[a] = 1
        b_dict = {}
        for b in B.split():
            if b in b_dict:
                b_dict[b] += 1
            else:
                b_dict[b] = 1
        res = []
        for k, v in a_dict.items():
            if v == 1 and k not in b_dict:
                res.append(k)
        for k, v in b_dict.items():
            if v == 1 and k not in a_dict:
                res.append(k)
        return res
