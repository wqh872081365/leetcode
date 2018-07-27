"""
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tem_dict = {}
        # nums_length_index = len(nums) / 2
        # for index, num in enumerate(nums, start=1):
        #     try:
        #         tem_dict[num] += 1
        #     except KeyError:
        #         tem_dict[num] = 1
        #     if index > nums_length_index:
        #         if tem_dict[num] > nums_length_index:
        #             return num

        result = None
        count = 0
        for num in nums:
            if count == 0:
                result = num
            if num == result:
                count += 1
            else:
                count -= 1
        return result
