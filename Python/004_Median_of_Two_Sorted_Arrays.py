"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        j = -1
        k = -1
        n_len = len(nums1) + len(nums2)
        if len(nums1) > 0 and len(nums2) > 0:
            for i in range(1, n_len + 1):
                if (((nums1[min((j + 1), len(nums1) - 1)] > nums2[min((k + 1), len(nums2) - 1)]) or (
                    j == len(nums1) - 1)) and (k != len(nums2) - 1)):
                    k = k + 1 if (k + 1) < (len(nums2) - 1) else len(nums2) - 1

                    if n_len / 2 * 2 == n_len:
                        if i == n_len / 2 + 1:
                            return (nums2[k] + number) / 2.0
                    else:
                        if i == n_len / 2 + 1:
                            return nums2[k]
                    number = nums2[k]

                else:
                    j = j + 1 if (j + 1) < (len(nums1) - 1) else len(nums1) - 1

                    if n_len / 2 * 2 == n_len:
                        if i == n_len / 2 + 1:
                            return (nums1[j] + number) / 2.0
                    else:
                        if i == n_len / 2 + 1:
                            return nums1[j]
                    number = nums1[j]
        elif len(nums2) == 0:
            return (nums1[n_len / 2 - 1] + nums1[n_len / 2]) / 2.0 if n_len / 2 * 2 == n_len else nums1[n_len / 2]
        elif len(nums1) == 0:
            return (nums2[n_len / 2 - 1] + nums2[n_len / 2]) / 2.0 if n_len / 2 * 2 == n_len else nums2[n_len / 2]