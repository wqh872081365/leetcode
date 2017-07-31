"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        else:
            result = {nums[0]: 1, nums[0]*-1: 1} if nums[0] != 0 else {nums[0]: 2}
            for i in range(1, len(nums)):
                tem_dict = {}
                for key in result:
                    tem_dict[key+nums[i]] = tem_dict.get(key+nums[i], 0) + result[key]
                    tem_dict[key-nums[i]] = tem_dict.get(key-nums[i], 0) + result[key]
                result = tem_dict
            return result.get(S, 0)