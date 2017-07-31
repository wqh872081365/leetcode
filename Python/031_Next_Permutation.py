"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums))[::-1]:
            if nums[i] > nums[i-1]:
                for j in range(i+1, len(nums)):
                    if nums[j] <= nums[i-1]:
                        nums[j-1], nums[i-1] = nums[i-1], nums[j-1]
                        nums[i:] = nums[i:][::-1]
                        return
                nums[len(nums)-1], nums[i-1] = nums[i-1], nums[len(nums)-1]
                nums[i:] = nums[i:][::-1]
                return
        nums[::] = nums[::-1]
        return