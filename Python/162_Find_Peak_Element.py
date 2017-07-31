"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -oo.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        elif len(nums) > 1:
            first = 0
            last = len(nums)-1
            while first < last-1:
                index = (first+last)/2
                if nums[index] > nums[index-1] and nums[index] > nums[index+1]:
                    return index
                elif nums[index] <= nums[index-1]:
                    last = index - 1
                else:
                    first = index + 1
            if first == last:
                return first
            else:
                if nums[first]>nums[last]:
                    return first
                else:
                    return last