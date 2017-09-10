"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        index = 1
        continuous_len = 1
        result = 1
        for i in range(1, len(nums)):
            if index:
                if nums[i] > nums[i-1]:
                    continuous_len += 1
                else:
                    index = 0
                    result = max(continuous_len, result)
            else:
                if nums[i] > nums[i-1]:
                    index = 1
                    continuous_len = 2
                else:
                    pass
        return max(continuous_len, result)