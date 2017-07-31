"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.result_list = []

        def node_list(node, index):
            if len(self.result_list) - 1 < index:
                self.result_list.append([node.val])
            else:
                self.result_list[index].append(node.val)
            if node.left:
                node_list(node.left, index + 1)
            if node.right:
                node_list(node.right, index + 1)

        node_list(root, 0)
        return [sum(i) / float(len(i)) for i in self.result_list]