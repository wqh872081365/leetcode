"""
You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]
"""


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = {}
        for num in nums:
            if num - 1 not in result:
                if num in result:
                    if 1 in result[num]:
                        result[num][1] += 1
                    else:
                        result[num][1] = 1
                else:
                    result[num] = {1: 1}
            else:
                if 2 in result[num - 1]:
                    result[num - 1][2] -= 1
                    if result[num - 1][2] == 0:
                        result[num - 1].pop(2)
                        if not result[num - 1]:
                            result.pop(num - 1)
                    if num in result:
                        if 3 in result[num]:
                            result[num][3] += 1
                        else:
                            result[num][3] = 1
                    else:
                        result[num] = {3: 1}
                elif 1 in result[num - 1]:
                    result[num - 1][1] -= 1
                    if result[num - 1][1] == 0:
                        result[num - 1].pop(1)
                        if not result[num - 1]:
                            result.pop(num - 1)
                    if num in result:
                        if 2 in result[num]:
                            result[num][2] += 1
                        else:
                            result[num][2] = 1
                    else:
                        result[num] = {2: 1}
                else:
                    result[num - 1][3] -= 1
                    if result[num - 1][3] == 0:
                        result[num - 1].pop(3)
                        if not result[num - 1]:
                            result.pop(num - 1)
                    if num in result:
                        if 3 in result[num]:
                            result[num][3] += 1
                        else:
                            result[num][3] = 1
                    else:
                        result[num] = {3: 1}
        if [1 for v in result.values() if 1 in v or 2 in v]:
            return False
        else:
            return True
