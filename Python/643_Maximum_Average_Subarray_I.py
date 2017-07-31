"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) > k:
            num_sum = sum(nums[0:k])
            max_sum = num_sum
            for i in range(1, len(nums)-k+1):
                num_sum += nums[i+k-1] - nums[i-1]
                max_sum = max(max_sum, num_sum)
            return max_sum/float(k)
        else:
            return sum(nums)/float(k)