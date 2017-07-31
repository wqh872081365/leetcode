"""
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums:
            self.s = [nums[0]]
            for num in nums[1:]:
                self.s.append(self.s[-1] + num)
        else:
            self.s = []

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.s[j] - self.s[i - 1] if i != 0 else self.s[j]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)