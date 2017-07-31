"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        sum = 0
        dict_sum = {0: 1}
        for num in nums:
            sum += num
            if sum-k in dict_sum:
                result += dict_sum[sum-k]
            dict_sum[sum] = dict_sum.get(sum, 0) + 1
        return result