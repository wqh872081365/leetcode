"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        if len(nums) < 3:
            return 0
        nums.sort()
        nums = [n for n in nums if n]
        for k in range(2, len(nums)):
            j = k - 1
            i = 0
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    result += (j - i)
                    j -= 1
                else:
                    i += 1
        return result