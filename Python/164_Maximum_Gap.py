"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""

import math

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        num_max = max(nums)
        num_min = min(nums)
        bucket_length = int(math.ceil((num_max - num_min) / (len(nums)-1))) or 1
        bucket_num = [[None, None] for _ in range((num_max - num_min)//bucket_length+1)]
        for i in nums:
            bucket = bucket_num[(i - num_min)//bucket_length]
            bucket[0] = i if bucket[0] == None else min(bucket[0], i)
            bucket[1] = i if bucket[1] == None else max(bucket[1], i)
        bucket_new = [b for b in bucket_num if b != [None, None]]
        if len(bucket_new) == 1:
            return bucket_new[0][1] - bucket_new[0][0]
        else:
            return max(bucket_new[i][0] - bucket_new[i-1][1] for i in range(1, len(bucket_new)))