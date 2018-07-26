"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tem_set = set()
        # for num in nums:
        #     if num in tem_set:
        #         tem_set.remove(num)
        #     else:
        #         tem_set.add(num)
        # return tem_set.pop()

        result = 0
        for num in nums:
            result ^= num
        return result
