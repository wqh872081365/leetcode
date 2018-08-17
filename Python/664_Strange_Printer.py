"""
There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.
"""


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        def get_number(start, end):
            if len(set(s_list[start: end+1])) == 1:
                return 1
            else:
                if (start, end) not in result_dict:
                    result = get_number(start, end-1) + 1
                    for i in range(start, end-1):
                        if s_list[end] == s_list[i]:
                            if i == start:
                                result_tem = get_number(start+1, end)
                            else:
                                result_tem = get_number(start, i-1) + get_number(i+1, end)
                            result = min(result, result_tem)
                    result_dict[(start, end)] = result
                    return result
                else:
                    return result_dict[(start, end)]

        result_dict = {}
        s_list = []
        if s:
            s_list.append(s[0])
        for i in s[1:]:
            if i != s_list[-1]:
                s_list.append(i)
        if s_list:
            return get_number(0, len(s_list)-1)
        else:
            return 0
