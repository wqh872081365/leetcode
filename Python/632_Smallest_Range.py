"""
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.
"""

import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = []
        pq = [[nums[i][0], i, 0] for i in range(len(nums))]
        heapq.heapify(pq)
        post = max([nums[i][0] for i in range(len(nums))])
        while pq:
            pre, i, j = heapq.heappop(pq)
            if not result or (post and result and post - pre < result[1] - result[0]):
                result = pre, post
            if j >= len(nums[i])-1:
                return result
            post = max(post, nums[i][j+1])
            heapq.heappush(pq, [nums[i][j+1], i, j+1])