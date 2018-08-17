"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s_list = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] < 0:
                s_list.append(i-1)
        change_time = 1
        for s in s_list:
            if s + 1 in s_list:
                return False
            else:
                if change_time <= 0:
                    return False
                res1 = True
                res2 = True
                if s - 1 >= 0:
                    if nums[s-1] > nums[s+1]:
                        res1 = False
                if s + 2 <= len(nums)-1:
                    if nums[s] > nums[s+2]:
                        res2 = False
                if res1 is False and res2 is False:
                    return False
                else:
                    change_time -= 1
        return True
