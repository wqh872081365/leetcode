"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sum = 0
        min_length = None
        for i in range(len(nums)):
            sum += nums[i]
            if sum >= s:
                while sum>=s:
                    sum -= nums[start]
                    start += 1
                length = i-start+2
                if ((not min_length) or (length < min_length)):
                    min_length = length
        return min_length if min_length else 0