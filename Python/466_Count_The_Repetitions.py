"""
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, "abc" can be obtained from "abdbec" based on our definition, but it can not be obtained from "acbbe".

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 <= n1 <= 106 and 1 <= n2 <= 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        count = 0
        index = 0
        s1_len = len(s1)
        s2_len = len(s2)
        repeat_list = []
        repeat = False
        for i in range(n1):
            comp = False
            for j, s1_sub in enumerate(s1):
                if s1_sub == s2[index]:
                    if index == 0:
                        if len(repeat_list) > 1:
                            if j in [rep[1] for rep in repeat_list]:
                                repeat_list.append([i, j])
                                comp = True
                                break
                        repeat_list.append([i, j])
                    index += 1
                if index >= s2_len:
                    count += 1
                    index = 0
            if comp:
                repeat = True
                for k in range(len(repeat_list))[-2::-1]:
                    if repeat_list[k][1] == repeat_list[-1][1]:
                        repeat_count = (n1 - repeat_list[-1][0]) / (repeat_list[-1][0] - repeat_list[k][0]) - 1
                        repeat_list[-1][0] += repeat_count * (repeat_list[-1][0] - repeat_list[k][0])
                        count += repeat_count * (len(repeat_list) - k - 1)
                        break
                break
        if repeat:
            for j in range(repeat_list[-1][1], s1_len):
                if s1[j] == s2[index]:
                    index += 1
                if index >= s2_len:
                    count += 1
                    index = 0
            for i in range(repeat_list[-1][0] + 1, n1):
                for j in range(s1_len):
                    if s1[j] == s2[index]:
                        index += 1
                    if index >= s2_len:
                        count += 1
                        index = 0
        return count / n2
