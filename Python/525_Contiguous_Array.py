"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        sum_nums = 1 if nums[0] else -1
        dict_sums = {(1 if nums[0] else -1): 0, 0: -1}
        max_length = 0
        for i in range(1, len(nums)):
            sum_nums += (1 if nums[i] else -1)
            if sum_nums in dict_sums:
                max_length = max(max_length, i-dict_sums[sum_nums])
            else:
                dict_sums[sum_nums] = i
        return max_length