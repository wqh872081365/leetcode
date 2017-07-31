"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        else:
            start = 0
            end = len(nums) - 1
            min_nums = None
            max_nums = None
            for i in range(1, len(nums)):
                if nums[i] >= nums[i-1]:
                    start = i
                else:
                    break
            for i in range(len(nums)-1)[::-1]:
                if nums[i] <= nums[i+1]:
                    end = i
                else:
                    break
            if start == len(nums)-1 or end == 0:
                return 0
            elif start - end == -1:
                min_nums = nums[end]
                max_nums = nums[start]
            else:
                min_nums = min(nums[start:end+1])
                max_nums = max(nums[start:end+1])
            for i in range(start+1):
                if nums[i] > min_nums:
                    start = i
                    break
            for i in range(end, len(nums))[::-1]:
                if nums[i] < max_nums:
                    end = i
                    break
            return end-start+1