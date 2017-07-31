"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1 = nums[0]
        max_2 = None
        max_3 = None
        min_1 = nums[0]
        min_2 = None
        for num in nums[1:]:
            if num > max_1:
                max_1, max_2, max_3 = num, max_1, max_2
            elif not max_2 or num > max_2:
                max_2, max_3 = num, max_2
            elif not max_3 or num > max_3:
                max_3 = num
            if num < min_1:
                min_1, min_2 = num, min_1
            elif not min_2 or num < min_2:
                min_2 = num
        return max(max_1*max_2*max_3, max_1*min_1*min_2)