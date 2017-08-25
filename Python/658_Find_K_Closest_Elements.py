"""
Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) == k:
            return arr
        index = max(abs(arr[0]-x), abs(arr[k-1]-x))
        for i in range(1, len(arr)-k+1):
            index_new = max(abs(arr[i]-x), abs(arr[k+i-1]-x))
            if index_new > index:
                break
            elif index_new == index:
                if abs(arr[i]-x) < abs(arr[k+i-1]-x):
                    break
                elif abs(arr[i]-x) == abs(arr[k+i-1]-x):
                    if not (arr[i] < x and arr[k+i-1] < x):
                        break
            else:
                index = index_new
        else:
            return arr[i:i+k]
        return arr[i-1:i+k-1]