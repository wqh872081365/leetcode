"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        pre_list = [nums[0], ]
        post_list = [nums[-1], ]
        for i in nums[1:]:
            pre_list.append(min(pre_list[-1], i))
        for j in range(1, len(nums)-1)[::-1]:
            if nums[j] > pre_list[j-1]:
                while post_list and post_list[-1] <= pre_list[j-1]:
                    post_list.pop()
                if post_list and post_list[-1] < nums[j]:
                    return True
            post_list.append(nums[j])
        return False