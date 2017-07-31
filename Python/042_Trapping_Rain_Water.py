"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        max_h_l = 0
        max_h_r = 0
        l = 0
        r = len(height)-1
        while(l <= r):
            max_h_l = max(max_h_l, height[l])
            max_h_r = max(max_h_r, height[r])
            if max_h_l < max_h_r:
                result += max_h_l-height[l]
                l += 1
            else:
                result += max_h_r-height[r]
                r -= 1
        return result