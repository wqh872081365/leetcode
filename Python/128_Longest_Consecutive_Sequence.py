"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        result = 0
        while nums_set:
            num = nums_set.pop()
            num_s = num
            while True:
                try:
                    nums_set.remove(num_s - 1)
                    num_s -= 1
                except KeyError:
                    break
            num_e = num
            while True:
                try:
                    nums_set.remove(num_e + 1)
                    num_e += 1
                except KeyError:
                    break
            result = max(result, num_e - num_s + 1)
        return result
