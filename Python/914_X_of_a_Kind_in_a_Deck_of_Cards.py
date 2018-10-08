"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]

Note:

1 <= deck.length <= 10000
0 <= deck[i] < 10000

"""


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        def get_gcd(a, b):
            if a == 1 or b == 1:
                return 1
            elif a == b:
                return a
            elif a > b:
                i = a % b
                if i:
                    return get_gcd(b, i)
                else:
                    return b
            else:
                i = b % a
                if i:
                    return get_gcd(a, i)
                else:
                    return a

        res = {}
        for d in deck:
            if d in res:
                res[d] += 1
            else:
                res[d] = 1
        index = None
        for r in res.values():
            if index is None:
                index = r
            elif index == 1:
                break
            else:
                index = get_gcd(index, r)
        return True if index > 1 else False
