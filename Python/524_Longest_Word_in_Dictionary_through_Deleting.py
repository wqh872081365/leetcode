"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        max_length = 0
        result = [""]
        for str_d in d:
            index = 0
            for i in s:
                if i == str_d[index]:
                    index += 1
                    if index == len(str_d):
                        break
            if index == len(str_d):
                if len(str_d) > max_length:
                    result = [str_d]
                    max_length = len(str_d)
                elif len(str_d) == max_length:
                    result.append(str_d)
        result = sorted(result)
        return result[0]