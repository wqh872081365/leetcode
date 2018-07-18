"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_max_index = len(nums) - 1
        start = 0
        end = nums_max_index
        result = [-1, -1]

        while start <= end:
            middle = (start + end) / 2
            if target == nums[middle]:
                start_left = start
                start_right = middle
                while start_left <= start_right:
                    start_middle = (start_left + start_right) / 2
                    if target == nums[start_middle]:
                        if start_middle == 0 or nums[start_middle - 1] != target:
                            result[0] = start_middle
                            break
                        else:
                            start_right = start_middle - 1
                    else:
                        start_left = start_middle + 1

                end_left = middle
                end_right = end
                while end_left <= end_right:
                    end_middle = (end_left + end_right) / 2
                    if target == nums[end_middle]:
                        if end_middle == nums_max_index or nums[end_middle + 1] != target:
                            result[1] = end_middle
                            break
                        else:
                            end_left = end_middle + 1
                    else:
                        end_right = end_middle - 1
                break
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return result
