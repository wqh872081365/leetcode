"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.result = 0

        def merge_sort(n):
            if len(n) <= 1:
                return n
            else:
                return merge(merge_sort(n[:len(n) / 2]), merge_sort(n[len(n) / 2:]))

        def merge(pre, post):
            pre_index = 0
            post_index = 0
            while pre_index < len(pre) and post_index < len(post):
                if pre[pre_index] <= 2 * post[post_index]:
                    pre_index += 1
                else:
                    self.result += len(pre) - pre_index
                    post_index += 1
            return sorted(pre + post)

        merge_sort(nums)
        return self.result