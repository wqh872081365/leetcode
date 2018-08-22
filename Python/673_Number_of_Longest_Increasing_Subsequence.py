"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
"""


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i, num in enumerate(nums):
            tem = [result[j] for j in range(i) if num > nums[j]]
            if tem:
                num_len = max([r[0] for r in tem]) + 1
                count = sum([r[1] for r in tem if r[0] == num_len - 1])
            else:
                num_len = 1
                count = 1
            result.append([num_len, count])
        if result:
            max_len = max([r[0] for r in result])
            return sum([r[1] for r in result if r[0] == max_len])
        else:
            return 0
