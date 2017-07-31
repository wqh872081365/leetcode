"""
Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        def check(num, sum_list, k):
            min_sum = sum_list[0]
            for i in range(len(sum_list) - k):
                min_sum = min(min_sum, sum_list[i] - i * num)
                if sum_list[i + k] - (i + k) * num - min_sum >= 0:
                    return True
            return False

        if len(nums) > k:
            sum_list = [0]
            for n in nums:
                sum_list.append(sum_list[-1] + n)

            if k < 100:
                max_ave = -1e6
                for j in range(k, min(2 * k, len(nums) + 1)):
                    for i in range(len(nums) - j + 1):
                        num_sum = sum_list[i + j] - sum_list[i]
                        max_ave = max(max_ave, num_sum / float(j))
                return max_ave

            lower = min(nums)
            upper = max(nums)
            while upper - lower > 1e-5:
                middle = (upper + lower) / 2.
                if check(middle, sum_list, k):
                    lower = middle
                else:
                    upper = middle
            return lower
        else:
            return sum(nums) / float(k)