"""
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        max_length = 0
        for num in nums:
            if d.get(num):
                d[num] += 1
            else:
                d[num] = 1
        for num in d.keys():
            if not d.get(num+1):
                continue
            else:
                max_length = max(max_length, d[num]+d[num+1])
        return max_length