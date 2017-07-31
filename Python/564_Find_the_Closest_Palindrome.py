"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.

"""

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        def near(n, index):
            if len(n)%2 == 0:
                if not index or n[:len(n)/2][::-1] != n[len(n)/2:]:
                    return n[:len(n)/2] + n[:len(n)/2][::-1]
                else:
                    return None
            else:
                if len(n) == 1:
                    return str(int(n)-1)
                else:
                    if not index or n[:len(n)/2][::-1] != n[len(n)/2+1:]:
                        return n[:len(n)/2+1] + n[:len(n)/2][::-1]
                    else:
                        return None
        if len(n) == 1:
            return str(int(n)-1)
        elif int(n) < 20 and int(n) >= 17:
            return "22"
        elif int(n) < 17 and int(n) > 12:
            return "11"
        elif int(n) < 12 and int(n) >= 10:
            return "9"
        elif int(n) == 10**(len(n)-1) or int(n) == 10**(len(n)-1) + 1:
            return str(10**(len(n)-1)-1)
        else:
            result = [near(str(int(n)-10**(len(n)/2)), 0), near(n, 1), near(str(int(n)+10**(len(n)/2)), 0)]
            result = [r for r in result if r != None]
            sub = [abs(int(r) - int(n)) for r in result]
            return result[sub.index(min(sub))]