"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 0:
            m = len(str(n))
            n_m = [int(str(n)[i]) for i in range(m)][::-1]
            l = []
            for i in range(m):
                if i == 0:
                    if n_m[i] == 0:
                        l.append((n / (10 ** (i + 1))))
                    else:
                        l.append((n / (10 ** (i + 1)) + 1))
                else:
                    if n_m[i] == 0:
                        l.append((n / (10 ** (i + 1))) * (10 ** i))
                    elif n_m[i] == 1:
                        l.append((n / (10 ** (i + 1))) * (10 ** i) + (n%(10**i)+1))
                    else:
                        l.append((n / (10 ** (i + 1)) + 1) * (10 ** i))
            return sum(l)
        else:
            return 0