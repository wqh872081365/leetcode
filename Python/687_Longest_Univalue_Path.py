"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = []

        def get_count(node, val):
            if node:
                if node.val == val:
                    return 1 + max(get_count(node.left, val), get_count(node.right, val))
                else:
                    count.append(1 + get_count(node.left, node.val) + get_count(node.right, node.val))
                    return 0
            else:
                return 0

        if root:
            count.append(1 + get_count(root.left, root.val) + get_count(root.right, root.val))
            return max(count) - 1
        else:
            return 0
